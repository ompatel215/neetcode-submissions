class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while  j < len(prices):
            cur = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
                profit = max(profit, cur)
        return profit

        
        