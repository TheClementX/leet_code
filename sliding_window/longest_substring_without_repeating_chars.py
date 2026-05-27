from typing import * 

def solution(s: str) -> int: 
    char_set = set()
    lo, max_len = 0, 0

    for hi in range(len(s)): 
        if hi > 0 and s[hi] in char_set: 
            while s[lo] != s[hi]: 
                if lo < hi: 
                    char_set.remove(s[lo])
                    lo += 1

            #handle the last lo which is the target letter
            char_set.remove(s[lo])
            lo += 1

        char_set.add(s[hi])
        cur_len = hi-lo+1 
        max_len = cur_len if cur_len > max_len else max_len

    return max_len


def test(solution: Callable[[str], int]): 
    s = "abcabcbb"
    sol = solution(s)
    print(sol)
    assert(sol == 3)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
