from typing import * 

def solution(n: int) -> bool: 
    num_set, cur_num = set(), str(n)
    
    while cur_num != "1" and cur_num not in num_set: 
        num_set.add(cur_num)
        next_num = 0
        for c in cur_num: 
            next_num += int(c) ** 2

        cur_num = str(next_num)

    return cur_num == "1"

def test(solution: Callable[[int], bool]): 
    n = 19
    assert(solution(n))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
