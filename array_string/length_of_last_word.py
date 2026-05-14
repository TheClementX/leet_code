from typing import * 

def solution(s: str) -> int: 
    strs = s.strip().split(" ")
    last_word = strs[-1].strip()
    return len(last_word)

def test(solution: Callable[[str], int]): 
    s = " fly me to  the moon "
    sol = solution(s)
    print(sol)
    assert(sol == 4)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
