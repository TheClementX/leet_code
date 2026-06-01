from typing import * 
from collections import deque

def solution(s: str) -> bool: 
    stack = []

    def matches(c1, c2): 
        match c1: 
            case '(': 
                return c2 == ')'
            case '{': 
                return c2 == '}'
            case '[': 
                return c2 == ']'

    for c in s: 
        if stack and matches(stack[-1], c): 
            stack.pop()
        else: 
            stack.append(c)

    return len(stack) == 0

def test(solution: Callable[[str], bool]): 
    s = "()[]{}"
    assert(solution(s))

    s = "(]"
    assert(not solution(s))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
