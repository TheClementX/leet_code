from typing import * 
import heapq

"""
not optimal solution, has an O(n) operation at each time step
"""
def solution(k: int, w: int, profits: list[int], capital: list[int]) -> int: 
    p_heap = [(-p, c) for p, c in zip(profits, capital)]
    heapq.heapify(p_heap)

    for i in range(k): 
        if not p_heap: return w

        rejected, found = [], False
        while p_heap: 
            p, c = heapq.heappop(p_heap)
            if c <= w: 
                found = True
                w += -p
                break
            rejected.append((p, c))

        if not found: return w
        p_heap.extend(rejected)
        heapq.heapify(p_heap)

    return w

"""
optimal solution: at each step performs up to N operations and a logn operation
"""
def solution(k: int, w: int, profits: list[int], capital: list[int]) -> int: 
    j_list = sorted([(-p, c) for p, c in zip(profits, capital)], key=lambda x: x[1])
    j_heap = []

    for i in range(k): 
        lo, hi = 0, len(j_list)
        while lo < hi and j_list[lo][1] <= w: 
            heapq.heappush(j_heap, j_list[lo])
            lo += 1
        j_list = j_list[lo:]

        if not j_heap: return w

        p, c = heapq.heappop(j_heap)
        w += -p

    return w

def test(solution): 
    k, w, = 2, 0
    profits  = [1,2,3]
    capital = [0,1,1]
    sol = solution(k, w, profits, capital)
    print(sol)
    assert(sol == 4)

    k, w, = 10, 0
    profits  = [1,2,3]
    capital = [0,1,2]
    sol = solution(k, w, profits, capital)
    print(sol)
    assert(sol == 6)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
