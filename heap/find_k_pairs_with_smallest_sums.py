from typing import * 
import heapq

def solution(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]: 
    m_heap = []
    result, i = [], 0
    h, w = len(nums1), len(nums2)
    visited = set()


    heapq.heappush(m_heap, (nums1[0]+nums2[0], 0, 0))
    while i < k and m_heap: 
        _, pr, pc = heapq.heappop(m_heap)
        result.append([nums1[pr], nums2[pc]])

        for dr, dc in [(0,1), (1,0)]: 
            nr, nc = pr+dr, pc+dc
            if nr < h and nc < w and (nr, nc) not in visited: 
                heapq.heappush(m_heap, (nums1[nr]+nums2[nc], nr, nc))
                visited.add((nr, nc))

        i += 1

    return result

def test(solution): 
    n1 = [1,7,11]
    n2 = [2,4,6]
    sol = solution(n1, n2, 13)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
