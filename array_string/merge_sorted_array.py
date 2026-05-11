from typing import List, Callable

def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
    """
    @requires len(nums1 = m + n)
    @ensures nums1 contains sorted merge of nums1 and nums2 in place
    """
    n1_idx = 0 
    n2_idx = 0 
    tmp_arr = list()

    #merge upto the smallest of nums1 and nums2 
    while n1_idx < m and n2_idx < n: 
        if nums1[n1_idx] <= nums2[n2_idx]: 
            tmp_arr.append(nums1[n1_idx])
            n1_idx += 1
        else: 
            tmp_arr.append(nums2[n2_idx])
            n2_idx += 1

    #handle leftover array segment if it exists
    while n1_idx < m: 
        tmp_arr.append(nums1[n1_idx])
        n1_idx += 1

    while n2_idx < n: 
        tmp_arr.append(nums2[n2_idx])
        n2_idx += 1

    #copy to nums1
    for i in range(m + n): 
        nums1[i] = tmp_arr[i] 

def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
    """
    @requires len(nums1 = m + n)
    @ensures nums1 contains sorted merge of nums1 and nums2 in place
    """
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0: 
        if nums1[i] >= nums2[j]: 
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else: 
            nums1[k] = nums2[j]
            k -= 1 
            j -= 1

    while i >= 0: 
        nums1[k] = nums1[i]
        k -= 1
        i -= 1

    while j >= 0: 
        nums1[k] = nums2[j]
        k -= 1
        j -= 1



def test(imp: Callable[[List[int], int, List[int], int], None]) -> None: 
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    imp(nums1, 3, nums2, 3)

    assert(nums1 == [1, 2, 2, 3, 5, 6])

    print("test cases passed")

test(merge2)




