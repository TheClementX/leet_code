from typing import * 

def solution(s: str, t: str) -> bool: 
    if len(s) != len(t): return False

    ds, dt = dict(), dict()
    for i in range(len(s)): 
        ds[s[i]] = ds.get(s[i], 0) + 1
        dt[t[i]] = dt.get(t[i], 0) + 1

    vs = sorted(list(ds.values())) 
    vt = sorted(list(dt.values())) 
    print(vs, vt)

    return vs == vt

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


    
