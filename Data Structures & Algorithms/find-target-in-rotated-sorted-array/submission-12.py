class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[r]:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if (nums[l] <= target <= nums[mid]) or (target <= nums[mid] <= nums[r]) or (nums[mid] <= nums[l] <= target):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

612345
456123
234561