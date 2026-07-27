from typing import * 

def solution(matrix: list[list[str]]) -> int: 
    if not matrix: return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    max_len = 0
    for r in range(1, m+1): 
        for c in range(1, n+1): 
            if matrix[r-1][c-1] == "1": 
                min_square = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
                dp[r][c] = 1 + min_square

            max_len = max(dp[r][c], max_len)

    return max_len * max_len


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
