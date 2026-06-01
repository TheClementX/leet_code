from typing import * 

def solution(intervals: List[List[int]]) -> List[List[int]]: 
    if len(intervals) <= 1: return intervals

    intervals = sorted(intervals, key=lambda x: x[0])

    result = [intervals[0]]
    for i in range(1, len(intervals)): 
        cur_start, cur_end = result[-1][0], result[-1][1]
        next_start, next_end = intervals[i][0], intervals[i][1]
        if cur_end >= next_start: 
            result[-1][1] = max(cur_end, next_end)
        else: 
            result.append(intervals[i])

    return result
    


def test(solution: Callable[[List[List[int]]], List[List[int]]]): 
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = solution(intervals)
    print(sol)
    assert(sol == [[1,6],[8,10],[15,18]])

    intervals = [[4,7],[1,4]]
    sol = solution(intervals)
    print(sol)
    assert(sol == [[1,7]])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
