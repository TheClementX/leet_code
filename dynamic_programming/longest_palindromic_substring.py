from typing import * 

def solution(s: str) -> str: 
    def find_palindrome(s, lo, hi): 
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]: 
            lo, hi = lo-1, hi+1
        return hi-lo-1

    lo, hi = 0, 0
    max_len = 0
    for i in range(len(s)): 
        l_odd  = find_palindrome(s, i, i)
        l_eve = find_palindrome(s, i, i+1)

        cur_len = max(l_odd, l_eve)
        if cur_len > max_len: 
            lo = i - ((cur_len-1) // 2)
            hi = i + (cur_len // 2)
            max_len = cur_len
        
    return s[lo:hi+1]

def test(solution): 
    s = "babad"
    sol = solution(s)
    print(sol)
    assert(sol == "bab")

    s = "cbbd"
    sol = solution(s)
    print(sol)
    assert(sol == "bb")

    s = "bb"
    sol = solution(s)
    print(sol)
    assert(sol == "bb")
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
