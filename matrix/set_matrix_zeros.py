from typing import * 

def solution(matrix: List[List[int]]) -> None: 
    zeros = []
    m, n = len(matrix), len(matrix[0])

    def set_zero(matrix, i, j, m , n): 
        for r in range(m): 
            matrix[r][j] = 0

        for c in range(n): 
            matrix[i][c] = 0

    for i in range(m): 
        for j in range(n): 
            if matrix[i][j] == 0: 
                zeros.append((i,j))

    for zero in zeros: 
        i, j = zero
        set_zero(matrix, i, j, m, n)

def solution(matrix: List[List[int]]) -> None: 
    rset, cset = set(), set()
    m, n = len(matrix), len(matrix[0])

    def set_row_zero(matrix, r, n): 
        for i in range(n): 
            matrix[r][i] = 0

    def set_col_zero(matrix, c, m): 
        for i in range(m): 
            matrix[i][c] = 0

    for i in range(m): 
        for j in range(n): 
            if matrix[i][j] == 0: 
                rset.add(i)
                cset.add(j)

    for r in rset: 
        set_row_zero(matrix, r, n)

    for c in cset: 
        set_col_zero(matrix, c, m)

def test(solution: Callable[[List[List[int]]], None]): 
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution(matrix)
    print(matrix)
    assert(matrix == [[1,0,1],[0,0,0],[1,0,1]])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
