class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.min.append(min(val, self.min[-1]) if self.min else val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
