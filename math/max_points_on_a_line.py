from typing import * 

def solution(points: list[list[int]]) -> int: 
    if len(points) == 1: return 1

    lines, cur_max = dict(), 0
    for i in range(len(points)): 
        for j in range(len(points)):
            if i == j: continue

            x1, y1 = points[i]
            x2, y2 = points[j]
            dx, dy = (x2-x1), (y2-y1)
            m = dy / dx if dx != 0 else float('inf')
            b = y1 - (m * x1) if dx != 0.0 else x1

            cur_line = lines.setdefault((m, b), set())
            cur_line.add((x1, y1))
            cur_line.add((x2, y2))
            cur_max = max(len(cur_line), cur_max)

    return cur_max

def test(solution): 
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    sol = solution(points)
    print(sol)
    assert(sol == 4)

    points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
    sol = solution(points)
    print(sol)
    assert(sol == 3)

    points = [[2,1],[2,2],[2,3],[3,1],[3,2],[3,3],[3,4]]
    sol = solution(points)
    print(sol)
    assert(sol == 4)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
