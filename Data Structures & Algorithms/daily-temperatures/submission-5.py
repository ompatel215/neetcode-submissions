class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t, i])
        return res



"""
30 38 30 36 35 40 28
0  1  2  3  4  5  6

stack = [[30, 0]]
"""
        