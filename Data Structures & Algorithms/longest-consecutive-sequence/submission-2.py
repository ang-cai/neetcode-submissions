class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lens = {}
        for i in range(len(nums)):
            if nums[i] not in lens:
                lens[nums[i]] = 1
                if nums[i] - 1 in lens:
                    lens[nums[i]] += lens[nums[i] - 1]
                if nums[i] + 1 in lens:
                    lens[nums[i]] += lens[nums[i] + 1]
                if nums[i] - 1 in lens:
                    lens[nums[i] - lens[nums[i] - 1]] = lens[nums[i]]
                if nums[i] + 1 in lens:
                    lens[nums[i] + lens[nums[i] + 1]] = lens[nums[i]]
        return max(lens.values())

