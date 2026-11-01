class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1

        while i < j:
            cur = (j - i) * min(heights[j], heights[i])
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
            
            res = max(res, cur)
        return res
        