from typing import * 

def solution(ratings: List[int]) -> int: 
    left, right = [0 for _ in range(len(ratings))], [0 for _ in range(len(ratings))]
    for i in range(len(ratings)): 
        #front calculation
        if i > 0 and ratings[i] > ratings[i-1]: 
            left[i] = left[i-1] + 1
        else: 
            left[i] = 1

        #back calculation
        bi = len(ratings)-i-1
        if bi < len(ratings)-1 and ratings[bi] > ratings[bi+1]: 
            right[bi] = right[bi+1] + 1
        else: 
            right[bi] = 1

    result = 0
    for i in range(len(left)): 
        result += max(left[i], right[i])

    return result


def test(solution: Callable[[List[int]], int]): 
    nums = [1,0,2,4,5,5,6,1,2]
    assert(solution(nums) == 18)

    nums = [1,2,2]
    assert(solution(nums) == 4)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


