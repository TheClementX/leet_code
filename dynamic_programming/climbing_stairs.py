from typing import * 

"""
bottom down
"""
def solution(n: int) -> int: 
    def ways(n, cache): 
        if n == 1: return 1
        if n == 2: return 2
    
        if n in cache: return cache[n]
        cache[n] = ways(n-1, cache) + ways(n-2, cache)

        print(cache)
        return cache[n]

    return ways(n, dict())

def solution(n: int) -> int: 
    if n == 1: return 1
    if n == 2: return 2

    cache = [1, 2]

    for i in range(3, n+1): 
        next = cache[0] + cache[1]
        cache[0] = cache[1]
        cache[1] = next

    return cache[-1]



def test(solution): 
    sol = solution(3)
    print(sol)

    sol = solution(4)
    print(sol)

    sol = solution(5)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
