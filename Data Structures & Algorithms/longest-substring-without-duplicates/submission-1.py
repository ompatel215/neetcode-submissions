class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        numSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in numSet:
                numSet.remove(s[l])
                l += 1
            numSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        