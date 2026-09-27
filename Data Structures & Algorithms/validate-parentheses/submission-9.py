class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in cto:
                if stack and cto[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        



        # []