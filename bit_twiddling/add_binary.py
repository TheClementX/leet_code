from typing import * 

def solution(a: str, b: str) -> str: 
    if len(b) < len(a): a, b = b, a
    a, b = a[::-1], b[::-1]

    result, i, r, = "", 0, 0
    while i < len(a): 
        n1, n2, = int(a[i]), int(b[i])
        v, r = (n1+n2+r) % 2, (n1+n2+r) // 2
        result += str(v)
        i += 1

    while i < len(b): 
        n = int(b[i])
        v, r = (n+r) % 2, (n+r) // 2
        result += str(v)
        i += 1

    if r == 1: 
        result += "1"

    return result[::-1]


def test(solution): 
    s1 = "000"
    s2 = "111"
    sol = solution(s1, s2)
    print(sol)
    assert(sol == "111")

    s1 = "1010"
    s2 = "1011"
    sol = solution(s1, s2)
    print(sol)
    assert(sol == "10101")

    s1 = "11"
    s2 = "1"
    sol = solution(s1, s2)
    print(sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
