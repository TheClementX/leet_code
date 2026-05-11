from typing import * 

def remove_element1(nums: List[int], val: int) -> int: 
    """
    @ensures the first k values of nums only contain values that are not val
    @return k where k is the number of valid elements
    """
    f, b = 0, len(nums)
    while f <= b: 
        if nums[f] == val: 
            nums[f] = nums[b-1]
            b -= 1
        else:
            f += 1 

    return f 

def remove_element2(nums: List[int], val: int) -> int: 
    """
    @ensures the first k values of nums only contain values that are not val
    @return k where k is the number of valid elements
    """
    k = 0 
    for i in range(len(nums)): 
        if nums[i] != val: 
            nums[k] = nums[i]
            k += 1

    return k


def test(imp: Callable[[List[int], int], int]): 
    nums = [3, 5, 3, 3, 5, 5, 3]
    val = 5
    imp(nums, val)
    print(nums)

    assert(nums[0:4] == [3, 3, 3, 3])

    print("all tests passed")

if __name__ == "__main__": 
    test(remove_element1) 

    test(remove_element2) 
