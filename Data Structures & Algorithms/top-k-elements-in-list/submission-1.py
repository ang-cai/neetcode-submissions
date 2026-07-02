import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        heap = []
        for num in frequency:
            heap.append((-frequency[num], num))
        heapq.heapify(heap)
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer