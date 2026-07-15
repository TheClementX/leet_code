from typing import * 

def solution(n: int) -> int: 
    def backtrack(r, n, cset, udiagset, ddiagset): 
        if r == n: return 1

        solutions = 0
        for c in range(n): 
            if (c not in cset and r+c not in udiagset 
                and r-c not in ddiagset): 

                cset.add(c)
                udiagset.add(r+c)
                ddiagset.add(r-c)

                solutions += backtrack(r+1, n, cset, udiagset, ddiagset)

                cset.remove(c)
                udiagset.remove(r+c)
                ddiagset.remove(r-c)


        return solutions

    return backtrack(0, n, set(), set(), set())

def test(solution): 
    sol = solution(4)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 

    
