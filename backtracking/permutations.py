from typing import * 

def solution(nums: list[int]) -> list[list[int]]: 
    def permutations(nums, cur, result): 
        if not nums: 
            result.append(list(cur))
            return result

        for i in range(len(nums)): 
            cur.append(nums[i])
            next_nums = nums[:i] + nums[i+1:]
            result = permutations(next_nums, cur, result)
            cur.pop()

        return result

    return permutations(nums, [], [])

def test(solution): 
    sol = solution([1,2])
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
