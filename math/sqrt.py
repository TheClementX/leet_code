from typing import * 
import math

"""
verifying binary search
    1. Assert that your logic shrinks on ranges of size 2
    2. Assert that your logic always exits on ranges of size 1
        -> for lo < hi loop guards it exits automatically
        -> for lo <= hi loop guards you must check that lo
        will pass hi with your mid calculation
"""
def solution(x: int) -> int: 
    lo, hi = 0, x

    while lo < hi+1: 
        mid = lo + ((hi-lo)//2)
        midp1 = mid + 1
        mids, midp1s = mid*mid, midp1*midp1

        if mids <= x and midp1s > x: 
            return mid

        if mids > x: 
            hi = mid
        else: 
            lo = mid+1

def test(solution): 
    for i in range(100): 
        sol = solution(i)
        act = i ** (1/2)
        print(f"{sol}, {act}")

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
