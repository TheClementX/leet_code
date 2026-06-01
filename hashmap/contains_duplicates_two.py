from typing import * 
from math import *

def solution(nums: List[int], k: int) -> bool: 
    idx_map = dict()

    for i in range(len(nums)): 
        num = nums[i]
        if num in idx_map: 
            for j in idx_map[num]: 
                if abs(i-j) <= k: 
                    return True
            idx_map[num].append(i)
        else: 
            idx_map[num] = [i]

    return False

def test(solution: Callable[[List[int], int], bool]): 
    nums = [1,2,3,1]
    k = 3
    assert(solution(nums, k))
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
