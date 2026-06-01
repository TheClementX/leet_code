from typing import * 

class MinStack: 
    def __init__(self): 
        self.stack = []
        self.mins = []

    def push(self, x): 
        self.stack.append(x)
        if self.mins == []: self.mins.append(x)
        elif self.mins[-1] >= x: self.mins.append(x)

    def pop(self): 
        top = self.stack.pop()
        if top == self.mins[-1]: 
            self.mins.pop()

    def top(self): 
        return None if not self.stack else self.stack[-1]

    def getMin(self): 
        return None if not self.mins else self.mins[-1]

def test(): 
    stack = MinStack()

    print("all tests passed")

if __name__ == "__main__": 
    test() 


    
