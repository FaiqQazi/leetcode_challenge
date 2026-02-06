class MinStack:

    def __init__(self):
        
        self.arr=[]
        self.min_arr=[]
        

    def push(self, val: int) -> None:
        if not self.min_arr or (val<=self.min_arr[-1]):
            self.min_arr.append(val)
        self.arr.append(val)
        

    def pop(self) -> None:
        if self.arr[-1]==self.min_arr[-1]:
            self.min_arr.pop()
        self.arr.pop()
        


    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()