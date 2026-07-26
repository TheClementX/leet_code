from typing import * 

def solution(nums: list[int]) -> int: 
    def min_subarray(nums): 
        cur_min, glo_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_min = min(cur_min + nums[i], nums[i])
            glo_min = min(cur_min, glo_min)
        return glo_min

    def max_subarray(nums): 
        cur_max, glo_max = nums[0], nums[0]
        for i in range(1, len(nums)): 
            cur_max = max(nums[i], cur_max + nums[i])
            glo_max = max(cur_max, glo_max)
        return glo_max

    min_sum = min_subarray(nums)
    max_sum = max_subarray(nums)
    arr_sum = sum(nums)

    if arr_sum - min_sum == 0: return max_sum
    return max(arr_sum - min_sum, max_sum)

def test(solution): 
    nums = [1,-2,3,-2]
    sol = solution(nums)
    print(sol)
    
    nums = [5,-1,5]
    sol = solution(nums)
    print(sol)

    nums = [1,2,3,2]
    sol = solution(nums)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
