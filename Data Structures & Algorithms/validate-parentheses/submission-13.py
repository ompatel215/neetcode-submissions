class Solution:
    def isValid(self, s: str) -> bool:
        cto = {"]":"[", "}":"{",")":"("}
        stack = []
        for c in s:
            if stack and c in cto and stack[-1] == cto[c]:
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False

        