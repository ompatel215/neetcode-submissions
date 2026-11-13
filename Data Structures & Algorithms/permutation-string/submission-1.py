class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        n = len(s1)
        l = 0

        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)

            # shrink window once it exceeds len(s1)
            if r - l + 1 > n:
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1

            if countS1 == countS2:
                return True

        return False