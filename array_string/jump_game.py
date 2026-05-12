from typing import * 

def solution(nums: list[int]) -> bool: 
    """
    O(n) my second solution
    """
    furthest = 0
    for i in range(len(nums)): 
        if furthest == i and nums[i] == 0: 
            return False
        if i + nums[i] > furthest and furthest >= i: 
            furthest = i + nums[i]
        if furthes >= len(nums)-1: 
            return True

    return True

def solution2(nums: list[int]) -> bool: 
    """
    O(n^2) my first solution using 0s as road blocks
    """
    if len(nums) == 1: return True

    def can_overcome(arr, hi, mx): 
        for i in range(hi): 
            dest = i + arr[i]
            if dest > hi or dest == mx: 
                return True
        return False

    for i in range(len(nums)): 
        if nums[i] == 0: 
            if not can_overcome(nums, i, len(nums)-1): 
                return False

    return True

def solution3(nums: list[int]) -> bool: 
    """
    O(n), cleanest solution from gemini
    """
    furthest = 0
    for i in range(len(nums)): 
        if i > furthest: 
            return False

        furthest = max(furthest, i + nums[i])

        if furthest >= len(nums)-1: 
            return True

    return True


def test(solution: Callable[[List[int]], bool]): 
    nums = [3,2,1,0,4]
    assert(solution(nums) == False)

    nums = [3,2,2,0,4]
    assert(solution(nums) == True)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
