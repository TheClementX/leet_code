from typing import * 

def solution(matrix: list[list[int]], target: int) -> bool: 
    def i_to_rc(i, h, w): 
        r = (i//w)
        c = i % w
        return r, c

    def search(lo, hi, target, matrix): 
        if lo >= hi: return False

        mid = lo + ((hi-lo)//2)
        
        r, c = i_to_rc(mid, len(matrix), len(matrix[0]))
        if matrix[r][c] > target: 
            return search(lo, mid, target, matrix)
        elif matrix[r][c] < target: 
            return search(mid+1, hi, target, matrix)

        return True
    
    m, n = len(matrix), len(matrix[0])
    return search(0, m*n, target, matrix)

def test(solution): 
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    sol = solution(matrix, target)
    print(sol)
    assert(sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
