from typing import * 

def solution(nums: list[int], target: int) -> int: 
    def find(lo, hi, target, nums): 
        if nums[lo] > target: return lo
        elif nums[hi-1] < target: return hi

        mid = lo + ((hi-lo)//2)
        if nums[mid] == target: return mid
        elif nums[mid] > target: 
            return find(lo, mid, target, nums)

        return find(mid+1, hi, target, nums)

    return find(0, len(nums), target, nums)

def test(solution): 
    nums = [1,3,5,6]
    sol = solution(nums, 5)
    print(sol)
    assert(sol == 2)

    nums = [1,3,5,6]
    sol = solution(nums, 2)
    print(sol)
    assert(sol == 1)

    nums = [1,3,5,6]
    sol = solution(nums, 4)
    print(sol)
    assert(sol == 2)

    nums = [1,3,5,6]
    sol = solution(nums, 7)
    print(sol)
    assert(sol == 4)

    nums = [1,3,5,6]
    sol = solution(nums, 0)
    print(sol)
    assert(sol == 0)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
