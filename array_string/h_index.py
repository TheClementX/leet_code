from typing import * 

def solution(citations: List[int]) -> int: 
    sc = sorted(citations)
    for i in range(len(sc)): 
        if len(sc) - i <= sc[i]: 
            return len(sc) - i 
    return 0

def test(solution: Callable[[List[int]], int]): 
    citations = [3,0,6,1,5]
    #[0,1,3,5,6]
    hi = solution(citations)
    print(hi)
    assert(hi == 3)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 
