from typing import * 
import sys
sys.setrecursionlimit(50000)

def solution(grid: list[list[int]]): 
    def dfs(grid, r, c): 
        if (r >= len(grid) or r < 0 or
            c >= len(grid[0]) or c < 0 or 
            grid[r][c] == 0): 
            return 0

        grid[r][c] = 0
        u_land = dfs(grid, r+1, c)
        d_land = dfs(grid, r-1, c)
        r_land = dfs(grid, r, c+1)
        l_land = dfs(grid, r, c-1)

        return (1 + u_land + d_land + r_land + l_land)

    max_land = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])): 
            if grid[r][c] == 1: 
                area = dfs(grid, r, c)
                max_land = max(area, max_land)

    return max_land

#iterative solution
def solution(grid: list[list[int]]): 
    def dfs(grid, r, c): 
        stack = [(r, c)] 
        area = 0

        while stack: 
            r, c = stack.pop()
            if (r < 0 or c < 0 or
                r >= len(grid) or c >= len(grid[0]) 
                or grid[r][c] == 0): 
                continue

            area += 1
            grid[r][c] = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                stack.append((r+dr, c+dc))

        return area

    max_land = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])): 
            if grid[r][c] == 1: 
                area = dfs(grid, r, c)
                max_land = max(area, max_land)

    return max_land

def test(solution): 
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    sol = solution(grid)
    print(sol)
#     assert(sol == 6)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
