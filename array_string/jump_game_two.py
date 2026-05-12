from typing import * 

def solution(nums: List[int]) -> int: 
    jmp_end = 0
    furthest = 0
    jmps = 0

    for i in range(len(nums)-1): 
        furthest = max(furthest, i + nums[i])
        if i == jmp_end: 
            jmp_end = furthest
            jmps += 1

    return jmps

def test(solution: Callable[[List[int]], int]): 
    nums = [2,3,1,1,4]
    print(solution(nums))
    assert(solution(nums) == 2)

    nums = [2,3,0,1,4]
    print(solution(nums))
    assert(solution(nums) == 2)

    nums = [5,2,1,3,0,6]
    print(solution(nums))
    assert(solution(nums) == 1)

    nums = [2,0,5,0,0,0]
    print(solution(nums))
    assert(solution(nums) == 2)

    nums = [1,2,3]
    print(solution(nums))
    assert(solution(nums) == 2)
    
    nums = [1,1,1,1]
    print(solution(nums))
    assert(solution(nums) == 3)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
