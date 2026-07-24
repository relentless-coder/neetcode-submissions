class MinStack:

    def __init__(self):
        self.main = []
        self.helper = []
        

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.helper or val <= self.helper[-1]:
            self.helper.append(val)

    def pop(self) -> None:
        val = self.main.pop()
        if self.helper[-1] == val:
            self.helper.pop()
        

    def top(self) -> int:
        return self.main[-1]
        

    def getMin(self) -> int:
        return self.helper[-1]
        
