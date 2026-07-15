from typing import * 

def solution(board: list[list[int]], word: str) -> bool: 
    def search(board, r, c, word, visited): 
        if word == "": return True
        if (r < 0 or c < 0 or 
            r >= len(board) or c >= len(board[0]) or
            (r,c) in visited): 
            return False
        l = board[r][c]
        if l != word[0]: return False
        
        visited.add((r,c))
        for dr, dc, in [(1,0),(-1,0),(0,1),(0,-1)]: 
            nr, nc = r+dr, c+dc
            if search(board, nr, nc, word[1:], visited): 
                return True
        visited.remove((r,c))

        return False

    for r in range(len(board)): 
        for c in range(len(board[0])): 
            if search(board, r, c, word, set()): 
                return True

    return False

def test(solution): 
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    sol = solution(board, word)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
