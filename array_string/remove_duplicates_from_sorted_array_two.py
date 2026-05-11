from typing import * 

def solution(nums: List[int]) -> int: 
    k = 0 
    for i in range(len(nums)): 
        if k < 2 or nums[k-2] < nums[i]: 
            nums[k] = nums[i]
            k += 1

    return k


def test(solution: Callable[[List[int]], int]): 
    nums = [1,1,2,2,2,3,3,4,5,5,5]
    k = solution(nums)
    print(nums)
    assert(k == 9)
    assert(nums == [1,1,2,2,3,3,4,5,5,5,5])

    nums = [0,0,1,1,1,1,2,3,3]
    k = solution(nums)
    print(nums)
    assert(k == 7)
    assert(nums == [0,0,1,1,2,3,3,3,3])

    nums = [0,0,1,1,1,1,2,3]
    k = solution(nums)
    print(nums)
    assert(k == 6)
    assert(nums == [0,0,1,1,2,3,2,3])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 
    
