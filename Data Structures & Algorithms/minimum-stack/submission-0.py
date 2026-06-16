class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return 2**31
        return self.stack[-1][1]
        
