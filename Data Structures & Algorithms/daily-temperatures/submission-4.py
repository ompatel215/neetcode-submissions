class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                res[stacki] = i-stacki
            stackt,stacki = stack.pop
            stack.append(i, t)

        stack = []
        """
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t, i))
        return res
        