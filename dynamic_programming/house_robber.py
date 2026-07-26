from typing import * 

def solution(nums: list[int]) -> int: 
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    if len(nums) == 3: return max(nums[0] + nums[2], nums[1])

    money = [nums[0], nums[1], nums[0]+nums[2]]
    cur_money = max(money)
    for i in range(3, len(nums)): 
        b2 = nums[i] + money[i-2]
        b3 = nums[i] + money[i-3]
        money.append(max(b2,b3))
        cur_money = max(cur_money, money[-1])

    return cur_money

def test(solution): 
    nums = [1,2,3,1]
    sol = solution(nums)
    print(sol)
    assert(sol == 4)

    nums = [2,7,9,3,1]
    sol = solution(nums)
    print(sol)
    assert(sol == 12)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
