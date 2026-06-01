from typing import * 

def solution(points: List[List[int]]) -> int: 
    points = sorted(points, key=lambda x: x[0])

    intersections = [points[0]]
    for i in range(1, len(points)): 
        if intersections[-1][1] >= points[i][0]: 
            #merge to only overlapping segment
            intersections[-1][0] = max(intersections[-1][0], points[i][0])
            intersections[-1][1] = min(intersections[-1][1], points[i][1])
        else: 
            intersections.append(points[i])


    return len(intersections)



def test(solution: Callable[[List[List[int]]], int]): 
    points = [[10,16],[2,8],[1,6],[7,12]]
    sol = solution(points)
    print(sol)
    assert(sol == 2)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
