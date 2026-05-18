from typing import * 

def solution(numbers: List[int], target: int) -> Tuple[int, int]: 
    """
    assumes a solution exists
    """
    lo, hi = 0, len(numbers)-1
    while lo < hi: 
        sum = numbers[lo] + numbers[hi]
        if sum == target: return (lo+1, hi+1)
        elif sum > target: hi -= 1
        else: lo += 1

    return (lo+1, hi+1)

def test(solution: Callable[[List[int], int], Tuple[int, int]]): 
    numbers = [2,7,11,15]
    target = 9
    sol = solution(numbers, target)
    print(sol)
    assert(sol == (1, 2))
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
