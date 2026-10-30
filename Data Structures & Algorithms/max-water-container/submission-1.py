class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0
        while i < j:
            cur = (j - i) * min(heights[i], heights[j])
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            res = max(res, cur)
        return res