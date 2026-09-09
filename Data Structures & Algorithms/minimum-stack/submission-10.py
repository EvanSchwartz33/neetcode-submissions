class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.Min:
            if val <= self.Min[-1]:
                self.Min.append(val)
        else:
            self.Min.append(val)
    def pop(self) -> None:
        if self.stack[-1] == self.Min[-1]:
            del self.Min[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]
