from typing import * 
from collections import * 

def solution(board: list[list[int]]) -> int: 
    #convert row col to boustrophedon
    #takes in standard convention r,c
    def rc_b(r, c, h, w): 
        r_bot = h-r-1
        b = (r_bot * w)
        if r_bot % 2 == 0: b += c + 1
        else: b += (w - c)
        return b

    #convert boustrophedon to row col
    #returns standard convention r,c
    def b_rc(b, h, w): 
        b -= 1
        r = b // w
        if r % 2 == 0: c = b % w
        else: c = w - 1 - (b % w)
        return h-r-1, c 

    h, w = len(board), len(board[0])
    moves, found = 0, False
    c_level, n_level = [(h-1, 0)], []
    visited = set([(h-1,0)])

    while c_level or n_level: 
        if not c_level: 
            moves += 1
            c_level, n_level = n_level, []

        cur_tile = c_level.pop()

        r, c = cur_tile
        b = rc_b(r, c, h, w)
        print(r, c, b)
        if b == h * w: 
            found = True
            break

        for i in range(1, 7): 
            nb = b + i
            nr, nc = b_rc(nb, h, w)
            if nr < 0 or nc < 0 or nr >= h or nc >= w: 
                continue
            if board[nr][nc] != -1: 
                nr, nc = b_rc(board[nr][nc], h, w)

            if (nr, nc) not in visited: 
                visited.add((nr, nc))
                n_level.append((nr, nc))

    return moves if found else -1

def solution(board: list[list[int]]) -> int: 
    #convert boustrophedon to row col
    #returns standard convention r,c
    def b_rc(b, h, w): 
        b -= 1
        r = b // w
        if r % 2 == 0: c = b % w
        else: c = w - 1 - (b % w)
        return h-r-1, c 

    h, w = len(board), len(board[0])
    queue = deque([(1, 0)])
    visited = set([1])

    while queue: 
        cur_tile, cur_move = queue.popleft()

        if cur_tile == h * w: 
            return cur_move

        for i in range(1, 7): 
            new_tile = cur_tile + i
            r, c = b_rc(new_tile, h, w)

            if r < 0 or c < 0 or r >= h or c >= w: 
                continue

            if board[r][c] != -1: 
                new_tile = board[r][c]

            if new_tile not in visited: 
                visited.add(new_tile)
                queue.append((new_tile, cur_move + 1))

    return -1

def test(solution): 
    board = [[-1,-1],[-1,3]]
    sol = solution(board)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
