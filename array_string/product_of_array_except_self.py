from typing import * 

def solution(nums: List[int]) -> List[int]: 
    output = [1 for _ in range(len(nums))] 

    #do prefixes
    pref = 1
    for i in range(len(nums)): 
        output[i] *= pref
        pref *= nums[i]

    suff = 1
    for i in range(len(nums)-1, -1, -1): 
        output[i] *= suff
        suff *= nums[i]

    return output

def solution2(nums: List[int]) -> List[int]: 
    """
    cleaner version of solution 1
    """
    output = [1 for _ in range(len(nums))] 

    pref, suff = 1, 1
    for i in range(len(nums)): 
        b_idx = len(nums) - i - 1
        output[i] *= pref
        output[b_idx] *= suff
        pref *= nums[i]
        suff *= nums[b_idx]

    return output


def test(solution: Callable[[List[int]], List[int]]): 
    nums = [1,2,3,4]
    sol = solution(nums)
    print(sol)
    assert(sol == [24,12,8,6])

    nums = [4]
    sol = solution(nums)
    print(sol)
    assert(sol == [1])
    
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
