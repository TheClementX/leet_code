from typing import * 

def solution(nums: List[int]) -> List[List[int]]: 
    nums = sorted(nums)
    result = []

    for i in range(len(nums)-2): 
        if i > 0 and nums[i] == nums[i-1]: 
            continue

        lo, hi = i+1, len(nums)-1
        target = -nums[i]
        while lo < hi: 
            sum = nums[lo] + nums[hi]

            if target == sum: 
                result.append([nums[i], nums[lo], nums[hi]])

                lo += 1
                hi -= 1

                while lo < hi and nums[lo] == nums[lo-1]: 
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]: 
                    hi -= 1
            elif sum > target: hi -= 1 
            else: lo += 1

    return result


def test(solution: Callable[[List[int]], List[List[int]]]): 
    nums = [-1, 0, 1, 2, -1, -4]
    sol = solution(nums)
    print(sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
