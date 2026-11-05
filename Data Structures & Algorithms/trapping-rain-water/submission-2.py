class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        LMax, RMax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                LMax = max(LMax, height[l])
                res += LMax - height[l]
            else:
                r -= 1
                RMax = max(RMax, height[r])
                res += RMax - height[r]
        return res
            
        