class MinStack(object):

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append(0)
            self.min = value
        else:
            self.stack.append(value - self.min)
            if value < self.min:
                self.min = value

    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        if len(self.stack) > 0:
            x = self.stack[-1]
            if x > 0:
                return x + self.min
            else:
                return self.min

    def getMin(self):
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()



