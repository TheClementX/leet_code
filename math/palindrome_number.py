from typing import * 

def solution(x: int) -> bool: 
    s1 = str(x)
    s2 = s1[::-1]
    return s1 == s2

"""
the actual best solution
"""
def solution(x: int) -> bool:
    if x < 0 or ((x % 10) == 0 and x != 0): 
        return False

    r = 0
    #works because reversed will equal x at some point
    while x > r: 
        r = (r * 10) + (x % 10)
        x //= 10

    return x == r or x == (r // 10)

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
