from typing import * 

def solution(grid: list[list[int]]): 
    def dfs(grid, r, c): 
        if (r >= len(grid) or r < 0 or
            c >= len(grid[0]) or c < 0 or 
            grid[r][c] == "0"): 
            return 

        grid[r][c] = "0"
        dfs(grid, r+1, c)
        dfs(grid, r-1, c)
        dfs(grid, r, c+1)
        dfs(grid, r, c-1)

    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])): 
            if grid[r][c] == "1": num_islands += 1
            dfs(grid, r, c)

    return num_islands


def test(solution): 
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    sol = solution(grid)
    print(sol)
    assert(sol == 1)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
