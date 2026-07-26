from typing import * 

def solution(s1: str, s2: str, s3: str) -> bool: 
    if len(s1) + len(s2) != len(s3): return False
    
    #string1 is y axis, string2 is x axis
    m, n = len(s1), len(s2)
    dp = [False for _ in range(n+1)]

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 and j == 0: 
                dp[j] = True
            # only s2
            elif i == 0: 
                dp[j] = dp[j-1] and s3[i+j-1] == s2[j-1]
            #only s1
            elif j == 0: 
                dp[j] = dp[j] and s3[i+j-1] == s1[i-1]
            else: 
                take1 = dp[j] and s1[i-1] == s3[j+i-1]
                take2 = dp[j-1] and s2[j-1] == s3[j+i-1]

                dp[j] = take1 or take2

    return dp[n]

def test(solution): 
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = solution(s1, s2, s3)
    print(sol)
    assert(sol)

    s1 = ""
    s2 = "b"
    s3 = "b"
    sol = solution(s1, s2, s3)
    print(sol)
    assert(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
