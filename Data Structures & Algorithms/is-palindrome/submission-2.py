class Solution:
    def AlNum(self, c):
        return (ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9')
                or ord('A') <= ord(c) <= ord('Z'))

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.AlNum(s[i]):
                i += 1
            while i < j and not self.AlNum(s[j]):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
        