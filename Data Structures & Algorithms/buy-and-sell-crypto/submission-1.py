class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l
        max_prices = 0
        while r < len(prices) - 1:
            while l + 1 < len(prices) and prices[l + 1] < prices[l]:
                l += 1
                r = l
            while r + 1 < len(prices) and prices[r] >= prices[l]:
                r += 1
                max_prices = max(max_prices, prices[r] - prices[l])
            l = r
        return max_prices