from typing import * 

def solution(s: str, t: str) -> bool: 
    if len(s) != len(t): return False

    map = dict()
    taken = set()
    for i in range(len(s)):
        m = map.get(s[i], -1)
        if m == -1 and t[i] in taken: 
            return False #return false if letter is already mapped
        if m == -1: 
            map[s[i]] = t[i]
            taken.add(t[i])
        elif m != t[i]:  
            return False

    return True

def test(solution: Callable[[str, str], bool]): 
    s, t = 'egg', 'add'
    assert(solution(s, t))

    s, t = 'papap', 'titii'
    assert(not solution(s, t))

    s, t = 'badc', 'baba'
    assert(not solution(s, t))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
