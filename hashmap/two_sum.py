from typing import * 

def solution(nums: List[int], target: int): 
    map = dict()
    for i in range(len(nums)): 
        dif = target - nums[i]
        if nums[i] in map: 
            return [map[nums[i]], i]
        else: 
            map[dif] = i

def test(solution: Callable[[List[int], int], List[int]]): 
    nums = [2,7,11,15]
    target = 9
    sol = solution(nums, 9)
    print(sol)
    assert(sol == [0,1])
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
