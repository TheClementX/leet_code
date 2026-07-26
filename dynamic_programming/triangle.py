from typing import * 

def solution(triangle: list[list[int]]) -> int: 
    lt = len(triangle)
    dp = [[0 for _ in range(lt-i)] for i in range(lt)]
    dp[0][0] = triangle[0][0]

    for i in range(1, lt): 
        cur_l = triangle[i]
        for j in range(len(cur_l)): 
            r, c = i-j, j
            cur_value = float('inf')
            for dr, dc in [(-1,0), (0,-1)]:
                br, bc = r+dr, c+dc
                if br >= 0 and bc >= 0: 
                    cur_value = min(cur_value, dp[br][bc]+triangle[i][j])
            dp[r][c] = cur_value

    min_path = float('inf')
    for i in range(lt): 
        r, c = lt-i-1, i
        min_path = min(min_path, dp[r][c])

    return min_path

def solution(triangle: list[list[int]]) -> int: 
    dp = triangle[-1][1]

    for r in range(len(triangle)-2, -1, -1): 
        for c in range(len(triangle[r])): 
            dp[col] = triangle[r][c] + min(dp[c], dp[c+1])

    return dp[0]

def test(solution): 
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sol = solution(triangle)
    print(sol)
    assert(sol == 11)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
