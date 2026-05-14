from typing import * 

def solution(haystack: str, needle: str) -> int: 
    h, n = len(haystack), len(needle)
    for i in range(h - n + 1): 
        if haystack[i:i+n] == needle: 
            return i

    return -1


def test(solution: Callable[[str, str], int]): 
    needle = "hello"
    haystack = "therehellothere"
    sol = solution(haystack, needle)
    print(sol)
    assert(sol == 5)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
