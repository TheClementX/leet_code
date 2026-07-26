from typing import * 

def solution(grid: list[list[int]]) -> int: 
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    #fill the first row
    for c in range(1, n): 
        dp[c] = dp[c-1] + grid[0][c]

    for r in range(1, m): 
        dp[0] += grid[r][0]
        for c in range(1, n): 
            dp[c] = grid[r][c] + min(dp[c], dp[c-1])

    return dp[-1]


def test(solution): 
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    sol = solution(grid)
    print(sol)
    assert(sol == 7)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
