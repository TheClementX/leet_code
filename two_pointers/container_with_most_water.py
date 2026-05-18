from typing import * 

def solution(height: List[int]) -> int: 
    lo, hi = 0, len(height)-1
    cur_vol_max = 0

    while lo < hi: 
        vol = min(height[lo], height[hi]) * (hi - lo)
        if vol > cur_vol_max: cur_vol_max = vol
        if height[lo] < height[hi]: lo += 1
        else: hi -= 1

    return cur_vol_max

def test(solution: Callable[[List[int]], int]): 
    height = [1,8,6,2,5,4,8,3,7]
    sol = solution(height)
    print(sol)

    height = [1,2,1]
    sol = solution(height)
    print(sol)
    assert(sol == 1)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
