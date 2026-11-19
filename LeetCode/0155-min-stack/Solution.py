class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.previousMin = []
    def push(self, value: int) -> None:
        self.stack.append(value)
        if value<=self.min:
            self.min = value
            self.previousMin.append(value)                     
    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.min:
            self.previousMin.pop()
            try:
                self.min = self.previousMin[-1]
            except:
                self.min = float('inf')
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()