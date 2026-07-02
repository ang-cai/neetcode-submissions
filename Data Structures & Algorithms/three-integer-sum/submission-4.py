class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j + 1] == nums[j]:
                        j += 1
                    while k - 1 > k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            while i + 1 < len(nums) - 2 and nums[i + 1] == nums[i]:
                i += 1    
            i += 1
        return answer    
