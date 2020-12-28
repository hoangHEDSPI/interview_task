class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        currentMin = self.getMin()
        if currentMin == None or currentMin > x:
            print(" >>> current Min: ", currentMin)
            print(" >>> x: ", x)
            currentMin = x
            print(" >>> current Min after changing :" , currentMin)
        self.stack.append((x, currentMin))
        print(" >>> stack: ", self.stack)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if len(self.stack) == 0:
             return None
        return self.stack[-1][1]


if __name__=="__main__":
    obj = MinStack()
    obj.getMin()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    x = obj.getMin()
    obj.pop()
    y = obj.getMin()
