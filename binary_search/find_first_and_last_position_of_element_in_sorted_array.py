from typing import * 

def solution(nums: list, target: int) -> list[int]: 
    if not nums: return [-1,-1]

    def find_left(nums, t): 
        lo, hi = 0, len(nums)
        while lo < hi: 
            mid = lo+((hi-lo)//2)
            if nums[mid] >= t: 
                hi = mid
            else: 
                lo = mid+1
        
        if lo < len(nums) and nums[lo] == t: 
            return lo
        return -1

    def find_right(nums, t): 
        lo, hi = 0, len(nums)

        while lo < hi: 
            mid = lo + ((hi-lo)//2)
            if nums[mid] <= t: 
                lo = mid+1
            else:
                hi = mid
        lo -= 1
        if lo < len(nums) and nums[lo] == t: 
            return lo
        return -1

    return [find_left(nums, target), find_right(nums, target)]



def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    def find_right(nums, t): 
        lo, hi = 0, len(nums)

        while lo < hi: 
            mid = lo + ((hi-lo)//2)
            if nums[mid] <= t: 
                lo = mid+1
            else:
                hi = mid
        lo -= 1
        if lo < len(nums) and nums[lo] == t: 
            return lo
        return -1

    nums = [1,2,3]
    for i in range(4):
        print(find_right(nums, i))
#     test(solution) 


    
