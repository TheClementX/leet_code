from typing import * 

def solution(nums: List[int]) -> int: 
    num_set = set(nums)

    best_len = 0
    for num in num_set: 
        if num-1 not in num_set: 
            cur_len = 1
            while num+1 in num_set: 
                cur_len += 1
                num += 1
            best_len = max(best_len, cur_len)

    return best_len


def test(solution: Callable[[List[int]], int]): 
    nums = [1,0,1,2]
    sol = solution(nums)
    print(sol)
    assert(sol == 3)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
