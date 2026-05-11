from typing import *

def remove_duplicates(nums: List[int]) -> int: 
    """
    @requires nums is an array sorted in non decreasing order 
    @ensures the first k elements of nums are sorted in non decreasing order and are unique
    """

    k = 0
    for i in range(1, len(nums)): 
        if nums[k] != nums[i]: 
            k += 1
            nums[k] = nums[i]

    return k + 1 



def test(imp: Callable[[List[int]], int]): 
    nums = [1, 1, 2, 2, 2, 3, 4, 5]
    k = imp(nums)
    assert(k == 5)
    assert(nums[0:k] == [1,2,3,4,5])

    nums = [1, 1, 2, 2, 2, 3, 4, 4]
    k = imp(nums)
    assert(k == 4)
    assert(nums[0:k] == [1,2,3,4])
    print("all tests passed")

if __name__ == "__main__": 
    test(remove_duplicates) 

    
