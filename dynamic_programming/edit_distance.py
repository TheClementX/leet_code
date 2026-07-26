from typing import * 

"""
taking from the upper diagonal is exactly the edit distance
of the previous word. Thus it makes sense if characters are
equal you would take the diagonal edit distance. 
"""
def solution(word1: str, word2: str) -> int: 
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 and j == 0: 
                dp[i][j] = 0
            elif i == 0: 
                same = 1 
                dp[i][j] = dp[i][j-1] + same
            elif j == 0: 
                same = 1 
                dp[i][j] = dp[i-1][j] + same
            else: 
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[m][n]

def test(solution): 
    word1 = 'horse'
    word2 = 'ros'
    sol = solution(word1, word2)
    print(sol)
    assert(sol == 3)

    word1 = ''
    word2 = 'a'
    sol = solution(word1, word2)
    print(sol)
    assert(sol == 1)

    word1 = 'a'
    word2 = 'aa'
    sol = solution(word1, word2)
    print(sol)
    assert(sol == 1)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
