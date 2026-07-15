from typing import * 

def solution(nums: list[int], target: int) -> int: 
    def find_min(lo, hi, nums): 
        if lo == hi: return lo

        mid = lo + ((hi-lo)//2)
        if nums[mid] > nums[hi]: 
            return find_min(mid+1, hi, nums)
        else:
            return find_min(lo, mid, nums)


    def search(lo, hi, k, target, nums): 
        if lo >= hi: return -1

        mid = lo + ((hi-lo)//2)
        r_mid = (mid + k) % len(nums)
        if nums[r_mid] > target: 
            return search(lo, mid, k, target, nums)
        elif nums[r_mid] < target: 
            return search(mid+1, hi, k, target, nums)

        return r_mid

    k = find_min(0, len(nums)-1, nums)
    return search(0, len(nums), k, target, nums)

def test(solution): 
    nums = [4,5,6,7,0,1,2]
    sol = solution(nums, 0)
    print(sol)
    assert(sol == 4)

    nums = [1,3,5]
    sol = solution(nums, 5)
    print(sol)
    assert(sol == 2)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 

    
