from typing import * 

def solution(nums: list[int]) -> int: 
    def find_min(lo, hi, nums): 
        if lo == hi: return nums[lo]

        mid = lo + ((hi-lo)//2)
        if nums[mid] > nums[hi]: 
            return find_min(mid+1, hi, nums)
        else:
            return find_min(lo, mid, nums)

    return find_min(0, len(nums)-1, nums)

def solution(nums: list[int]) -> int: 
    def find_min(lo, hi, nums): 
        if hi-lo <= 1: 
            return nums[lo]
        mid = lo + ((hi-lo)//2)

        if nums[mid] > nums[hi-1]: 
            return find_min(mid+1, hi, nums)
        else:
            return find_min(lo, mid+1, nums)

    return find_min(0, len(nums), nums)

def test(solution): 
    nums = [3,4,5,1,2]
    sol = solution(nums)
    print(sol)
    assert(sol == 1)
    
    nums = [4,5,6,7,0,1,2]
    sol = solution(nums)
    print(sol)
    assert(sol == 0)

    nums = [11,13,15,17]
    sol = solution(nums)
    print(sol)

    assert(sol == 11)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 

    
