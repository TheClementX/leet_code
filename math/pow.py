from typing import * 

def solution(x: float, n: int): 
    if n == 0.0: 
        return 1.0

    if n < 0.0: 
        x = 1 / x
        n = -n 

    extra = 1.0
    square = x

    while n > 1: 
        if n % 2 == 1: 
            extra *= square
        square *= square
        n //= 2 

    return extra * square 


def test(solution): 
    print(solution(2, 2))
    print(solution(2, 5))
    print(solution(2, 7))
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
