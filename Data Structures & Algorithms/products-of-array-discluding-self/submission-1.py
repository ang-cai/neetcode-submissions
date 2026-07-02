class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(len(nums)-1):
            left.append(left[i]*nums[i])
        right = [1]
        for i in range(len(nums)-1):
            right.append(right[i]*nums[len(nums)-1-i])
        answer = []
        for i in range(len(nums)):
            answer.append(left[i] * right[len(nums)-1-i])
        return answer