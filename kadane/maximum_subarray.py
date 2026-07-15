from typing import * 

def solution(nums: list[int]): 
    cur_max, glo_max = nums[0], nums[0]

    for i in range(1, len(nums)): 
        cur_max = max(nums[i], cur_max + nums[i])
        glo_max = max(cur_max, glo_max)

    return glo_max

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
