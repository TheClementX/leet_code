from typing import * 

def solution(board: list[list[str]]) -> None: 
    def flip(board, r, c): 
        stack, cache = [(r, c)], []
        visited = set()

        has_edge = False
        while stack: 
            pos = stack.pop()
            if pos in visited: continue
            visited.add(pos)
            r, c = pos

            if (r < 0 or c < 0 or 
                r >= len(board) or c >= len(board[0])): 
                has_edge = True
                continue
            if board[r][c] == "X": continue

            cache.append(pos)
            for dr, dc, in [(1,0), (-1,0), (0,1), (0,-1)]: 
                stack.append((r+dr, c+dc))

        if not has_edge: 
            for r, c in cache: 
                board[r][c] = "X"

    for r in range(len(board)): 
        for c in range(len(board[0])): 
            if board[r][c] == "O": 
                flip(board, r, c)

def test(solution): 
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    sol = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    solution(board)
    assert(board == sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
