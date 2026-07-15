from typing import * 

def solution(nums: list[int]) -> int: 
    def find(lo, hi, nums): 
        if lo >= hi: return None

        mid = lo + ((hi-lo)//2)
        if mid+1 < len(nums) and nums[mid+1] > nums[mid]: 
            return find(mid+1, hi, nums)
        elif mid-1 >= 0 and nums[mid-1] > nums[mid]: 
            return find(lo, mid, nums)

        return mid

    return find(0, len(nums), nums)


def test(solution): 
    nums = [1]
    sol = solution(nums)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
