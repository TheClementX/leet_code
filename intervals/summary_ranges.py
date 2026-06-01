from typing import * 

def solution(nums: List[int]) -> List[str]: 
    if nums == []: return []

    result = []
    cur_start, prev = nums[0], nums[0]
    for i in range(1, len(nums)): 
        if nums[i]-1 != prev: 
            if cur_start == prev: 
                result.append(str(prev))
            else: 
                result.append(f"{cur_start}->{prev}")
            cur_start = nums[i]
        prev = nums[i]

    #append last interval  
    if cur_start == prev: 
        result.append(str(prev))
    else: 
        result.append(f"{cur_start}->{prev}")

    return result



def test(solution: Callable[[List[int]], List[str]]): 
    nums = [0,1,2,4,5,7]
    sol = solution(nums)
    print(sol)
    assert(sol == ["0->2","4->5","7"])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
