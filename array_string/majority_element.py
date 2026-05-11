from typing import * 

def solution(nums: List[int]) -> int: 
    counts = dict()
    cur_max = -1 
    cur_max_key = None

    for num in nums: 
        counts[num] = counts.get(num, 0) + 1
        if c_count > cur_max: 
            cur_max_key = num
            cur_max = c_count

        counts[num] = c_count

    return cur_max_key

def test(solution: Callable[[List[int]], int]): 
    nums = [1,1,1,2,2]
    me = solution(nums)
    assert(me == 1)

    nums = [3,2,3]
    me = solution(nums)
    assert(me == 3)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 

    
