from typing import * 

def solution(s: str) -> bool: 
    s = s.strip().lower()
    lo, hi = 0, len(s)-1
    while lo < hi: 
        if not s[lo].isalnum(): lo += 1
        if not s[hi].isalnum(): hi -= 1

        if s[lo].isalnum() and s[hi].isalnum() and s[hi] != s[lo]: 
            return False
        elif s[lo].isalnum() and s[hi].isalnum() and s[hi] == s[lo]: 
            lo += 1
            hi -= 1

    return True

def test(solution: Callable[[str], bool]): 
    s = "A man, a plan, a canal: Panama"
    assert(solution(s) == True)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
