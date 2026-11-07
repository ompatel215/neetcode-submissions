class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0

        while j < len(prices):
            profit = prices[j] - prices[i]
            if prices[i] > prices[j]:
                i = j
                j += 1
            
            else:
                j += 1

            res = max(res, profit)
        return res