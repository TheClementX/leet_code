from typing import * 

def solution(target: int, nums: List[int]) -> int: 
    lo, sum, min_len = 0, 0, len(nums)+1

    for hi in range(len(nums)): 
        sum += nums[hi]
        if sum >= target: 
            while sum - nums[lo] >= target: 
                sum -= nums[lo]
                lo += 1 

            sub_len = (hi-lo+1)
            min_len = sub_len if sub_len < min_len else min_len


    return min_len if min_len != (len(nums)+1) else 0

def solution2(target: int, nums: List[int]) -> int: 
    """
    different but functionally equivalent loop structure
    """
    lo, sum, min_len = 0, 0, len(nums)+1
    for hi in range(len(nums)): 
        sum += nums[hi]
        if sum >= target: 
            while sum >= target: 
                sum -= nums[lo]
                lo += 1 

            sub_len = (hi-lo+1) + 1 
            min_len = sub_len if sub_len < min_len else min_len


    return min_len if min_len != (len(nums)+1) else 0

def test(solution: Callable[[int, List[int]], int]): 
    nums = [2,3,1,2,4,3]
    #      [0,1,2,3,4,5]
    target = 7
    sol = solution(target, nums)
    print(sol)
    assert(sol == 2)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
