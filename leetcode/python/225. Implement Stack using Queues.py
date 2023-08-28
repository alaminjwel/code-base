class MyStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.data.pop()        

    def top(self) -> int:
        if self.empty():
            return None
        return self.data[-1]        

    def empty(self) -> bool: 
        if len(self.data)==0:
            return True
        return False
        

obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2,param_3,param_4)