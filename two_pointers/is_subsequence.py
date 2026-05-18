from typing import * 

def solution(s: str, t: str) -> bool: 
    if len(s) > len(t): return False
    s_i = 0

    for i in range(len(t)): 
        if s_i >= len(s): return True
        if t[i] == s[s_i]: 
            s_i += 1

    return s_i >= len(s)

def test(solution: Callable[[str, str], bool]): 
    s = 'abc'
    t = 'ahbgdc'
    assert(solution(s, t))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
