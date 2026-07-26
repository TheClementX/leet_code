from typing import * 

"""
legendre's formula 
"""
def solution(n: int) -> int: 
    zeros = 0
    while n > 0: 
        n //= 5
        zeros += n

    return zeros

def test(solution): 
    for i in range(20): 
        print(f"{i}: {solution(i)}")
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
