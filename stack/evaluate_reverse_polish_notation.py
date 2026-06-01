from typing import * 
from math import *

def solution(tokens: str) -> int: 
    stack = []

    for t in tokens: 
        if t == '+' and len(stack) >= 2: 
            v1, v2 = stack.pop(), stack.pop()
            stack.append(v2 + v1)
        elif t == '-' and len(stack) >= 2:
            v1, v2 = stack.pop(), stack.pop()
            stack.append(v2 - v1)
        elif t == '*' and len(stack) >= 2:
            v1, v2 = stack.pop(), stack.pop()
            stack.append(v2 * v1)
        elif t == '/' and len(stack) >= 2:
            v1, v2 = stack.pop(), stack.pop()
            stack.append(trunc(v2 / v1))
        else: 
            stack.append(int(t))

    return stack[-1]

def test(solution: Callable[[str], int]): 
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = solution(tokens)
    print(sol)
    assert(sol == 22)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
