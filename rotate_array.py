from typing import * 

def solution(nums: List[int], k: int) -> None: 
    k = k % len(nums)
    def reverse(arr, lo, hi): 
        i, j, = lo, hi-1
        while i < j: 
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1

    reverse(nums, 0, len(nums))
    reverse(nums, 0, k)
    reverse(nums, k, len(nums))

def solution2(nums: List[int], k: int) -> None: 
    """
    @Note: this solution only works for odd length arrays
    """
    idx = 0
    val = nums[idx]
    for i in range(len(nums)): 
        idx = (idx + k) % len(nums)
        tmp = nums[idx]
        nums[idx] = val 
        val = tmp

def test(solution: Callable[[List[int], int], None]): 
    nums = [1,2,3,4,5,6,7]
    k = 2
    solution(nums, k)
    print(nums)
    assert(nums == [6,7,1,2,3,4,5])

    nums = [1,2,3,4]
    k = 2
    solution(nums, k)
    print(nums)
    assert(nums == [3,4,1,2])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 

    
