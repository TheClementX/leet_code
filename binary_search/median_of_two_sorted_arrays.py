from typing import * 

def solution(nums1: list[int], nums2: list[int]) -> float: 
    if len(nums1) > len(nums2): 
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)
    half = total // 2

    lo, hi = 0, len(nums1)
    while True: 
        mid1 = lo + ((hi-lo)//2)
        mid2 = half - mid1

        n1left = nums1[mid1-1] if mid1-1 >= 0 else float("-inf")
        n1right = nums1[mid1] if mid1 < len(nums1) else float("inf")
        n2left = nums2[mid2-1] if mid2-1 >= 0 else float("-inf")
        n2right = nums2[mid2] if mid2 < len(nums2) else float("inf")

        if n1left <= n2right and n2left <= n1right: 
            break
        elif n1left > n2right: 
            hi = mid1-1
        elif n2left > n1right: 
            lo = mid1+1

    if total % 2 == 0: 
        return (max(n1left, n2left) + min(n1right, n2right)) / 2
    return float(min(n1right, n2right))

def test(solution): 
    nums1 = [1,3]
    nums2 = [2]
    sol = solution(nums1, nums2)
    print(sol)
    assert(sol == 2.0)

    nums1 = [1,2,5,6,9]
    nums2 = [3,8,9,10]
    sol = solution(nums1, nums2)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
