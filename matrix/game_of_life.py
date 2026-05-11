from typing import * 

def solution(board: List[List[int]]) -> None: 
    """
    @note 0 == dead 1 == alive 2 == dead -> alive 3 == alive -> dead
    """
    def get_nbors(board, r, c, mr, mc): 
        """
        get the neighbors of a square at r, c treat out of index positions 
        as dead
        """
        nbors = 0
        for dr in [-1, 0, 1]: 
            for dc in [-1, 0, 1]: 
                cr, cc = r + dr, c + dc
                if ((r != cr or c != cc) and (cr >= 0 and cc >= 0) 
                    and (cr < mr and cc < mc)
                    and (board[cr][cc] == 1 or board[cr][cc] == 3)): 
                    nbors += 1

        return nbors

    def set_next_state(board, r, c): 
        """
        if a state remains alive or dead leave the state
        if dead -> live write 2
        if live -> dead write 3
        """
        nbors = get_nbors(board, r, c, len(board), len(board[0]))
        alive = board[r][c] == 1

        if alive and (nbors < 2 or nbors > 3): 
            board[r][c] = 3
        elif not alive and nbors == 3: 
            board[r][c] = 2

    def update(board): 
        """
        flip 2 -> 1 and 3 -> 0 to set dead / alive status properly
        """
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if board[r][c] == 2: 
                    board[r][c] = 1
                if board[r][c] == 3: 
                    board[r][c] = 0

    for r in range(len(board)): 
        for c in range(len(board[0])): 
            set_next_state(board, r, c)

    update(board)


def test(solution: Callable[List[List[int]], None]): 
    board  = [
        [0,1,0], 
        [0,0,1], 
        [1,1,1], 
        [0,0,0]
    ]
    res = [
        [0,0,0],
        [1,0,1],
        [0,1,1],
        [0,1,0]
    ]
    solution(board)
    print(board)
    assert(board == res)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 
