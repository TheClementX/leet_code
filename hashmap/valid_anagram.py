from typing import * 

def solution(s: str, t: str) -> bool: 
    sd, td = dict(), dict()
    for c in s: 
        sd[c] = sd.get(c, 0) + 1

    for c in t: 
        td[c] = td.get(c, 0) + 1

    return td == sd

def test(solution: Callable[[str, str], bool]): 
    s, t = 'anagram', 'nagaram'
    assert(solution(s, t))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
