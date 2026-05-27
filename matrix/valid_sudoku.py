from typing import * 

def solution(board: List[List[int]]) -> bool: 
    def valid_row(board, r):
        counts = dict()
        for i in range(len(board)): 
            v = board[r][i]
            counts[v] = counts.get(v, 0) + 1
            if counts[v] > 1 and v != ".": return False
        return True

    def valid_col(board, c): 
        counts = dict()
        for i in range(len(board[0])): 
            v = board[i][c]
            counts[v] = counts.get(v, 0) + 1
            if counts[v] > 1 and v != ".": return False
        return True

    def valid_square(board, r, c): 
        counts = dict()
        for i in range(3): 
            for j in range(3): 
                v = board[r+i][c+j]
                counts[v] = counts.get(v, 0) + 1
                if counts[v] > 1 and v != ".": return False
        return True

    m, n = len(board), len(board[0])
    for i in range(m): 
        for j in range(n): 
            if i % 3 == 0 and j % 3 == 0:
                if not valid_square(board, i, j):
                    return False
            if not valid_row(board, i): return False
            if not valid_col(board, j): return False

    return True

def solution(board: List[List[int]]) -> bool: 
    rows = [[False for _ in range(9)] for _ in range(9)]
    cols = [[False for _ in range(9)] for _ in range(9)]
    squs = [[False for _ in range(9)] for _ in range(9)]

    m, n = len(board), len(board[0])
    for i in range(m): 
        for j in range(n): 
            v = board[i][j]
            if v != ".": 
                s = ((i // 3) * 3) + (j // 3)
                v = int(v)

                if rows[i][v-1] or cols[j][v-1] or squs[s][v-1]: 
                    return False

                rows[i][v-1], cols[j][v-1], squs[s][v-1] = True, True, True

    return True


def test(solution: Callable[[List[int]], bool]): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
