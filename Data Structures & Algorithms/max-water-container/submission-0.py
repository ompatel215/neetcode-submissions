class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        i, j = 0, len(heights) - 1

        while i < j:
            curArea = (j - i) * min(heights[j], heights[i])
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
                
            maxA = max(maxA, curArea)
        return maxA
        