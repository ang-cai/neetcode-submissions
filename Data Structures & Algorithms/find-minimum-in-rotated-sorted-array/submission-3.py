class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r - 1:
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]