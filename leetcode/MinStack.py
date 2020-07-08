class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.size = 0
        
        

    def push(self, x: int) -> None:
        if(self.size == 0):
            self.min.append(x)
        else:
            if(x <= self.min[-1]):
                self.min.append(x)
        self.size += 1
        self.stack.append(x)
        

    def pop(self) -> None:
        tmp = self.stack.pop()
        if(tmp == self.min[-1]):
            self.min.pop()
        self.size -= 1
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
