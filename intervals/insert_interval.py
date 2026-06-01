from typing import * 

def solution(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
    if intervals == []: return [newInterval]

    #insert interval
    inserted = False
    for i in range(0, len(intervals)): 
        if newInterval[0] < intervals[i][0]: 
            intervals.insert(i, newInterval)
            inserted = True

    if not inserted: result.append(newInterval)

    print(intervals)
        
    #merge interval
    result = [intervals[0]]
    for i in range(1, len(intervals)): 
        cur_start, cur_end = result[-1][0], result[-1][1]
        next_start, next_end = intervals[i][0], intervals[i][1]
        if cur_end >= next_start: 
            result[-1][1] = max(cur_end, next_end)
        else: 
            result.append(intervals[i])

    return result

def solution(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
    if intervals == []: return [newInterval]

    result, i = [], 0 
    while i < len(intervals) and intervals[i][1] < newInterval[0]: 
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and newInterval[1] >= intervals[i][0]: 
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    while i < len(intervals): 
        result.append(intervals[i])
        i += 1

    return result



def test(solution): 
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    sol = solution(intervals, newInterval)
    print(sol)
    assert(sol == [[1,5],[6,9]])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
