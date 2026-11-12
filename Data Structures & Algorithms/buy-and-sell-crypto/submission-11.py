class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        res = 0

        while j < len(prices):
            if prices[j] > prices[i]:
                res = max(res, prices[j] - prices[i])
            else:
                i = j
            
            j += 1
            
        
        return res