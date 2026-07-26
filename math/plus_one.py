from typing import * 

def solution(digits: list[int]) -> list[int]: 
    r = 1
    for i in range(len(digits)-1, -1, -1): 
        if digits[i] + r < 10: 
            digits[i] += r
            r = 0 
            break
        digits[i] = 0

    if r == 1: 
        digits.insert(0, 1)

    return digits
        

def test(solution): 
    digits = [9,9,9]
    sol = solution(digits)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
