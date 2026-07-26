from typing import * 
import heapq

#bad solution
def solution(nums: list[int], k: int) -> int: 
    for i in range(len(nums)): 
        nums[i] *= -1

    heapq.heapify(nums)
    kth = None
    for i in range(k): 
        kth = -1 * heapq.heappop(nums)

    return kth

#optimal heap solution
def solution(nums: list[int], k: int) -> int: 
    heap = nums[:k]

    for n in nums[k:]: 
        if n > heap[0]: 
            heapq.heappoppush(heap, n)

    return heap[0]

#quickselect is another option for solving this problem

def test(solution): 
    nums = [3,2,1,5,6,4]
    k = 2
    sol = solution(nums, k)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
