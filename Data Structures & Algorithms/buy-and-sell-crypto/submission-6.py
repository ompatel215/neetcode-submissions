class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                curP = prices[j] - prices[i]
                profit = max(profit, curP)
            else:
                i = j
            j += 1
        return profit