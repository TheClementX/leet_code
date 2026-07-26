from typing import * 

"""
top down solution
"""
def solution(nums: list[int]) -> int: 
    def dfs(i, nums, cache): 
        max_nums = 1
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]: 
                if j not in cache: 
                    cache[j] = dfs(j, nums, cache)
                cur_nums = 1 + cache[j]
                max_nums = max(cur_nums, max_nums)

        return max_nums
    
    best_len = 1
    for i in range(len(nums)): 
        cur_len = dfs(i, nums, dict())
        best_len = max(best_len, cur_len)

    return best_len

"""
bottom up solution
"""
def solution(nums: list[int]) -> int: 
    dp = [1] * len(nums)

    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            if nums[j] > nums[i]: 
                dp[j] = max(dp[j], dp[i]+1)

    return max(dp)


def test(solution): 
    nums = [10,9,2,5,3,7,101,18]
    sol = solution(nums)
    print(sol)
    assert(sol == 4)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
