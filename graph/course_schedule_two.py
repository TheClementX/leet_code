from typing import * 

def solution(numCourses: int, prerequisites: list[list[int]]): 
    #graph stores a node and all the nodes it goes out to 
    graph, num_edges = dict(), dict()

    for a, b in prerequisites: 
        b_out = graph.setdefault(b, [])
        b_out.append(a)
        num_edges[a] = num_edges.get(a, 0) + 1

    nodes = deque()
    for i in range(0, numCourses): 
        if i not in num_edges: 
            nodes.append(i)

    courses_taken = 0
    result = []
    while nodes:
        cur_course = nodes.popleft()
        courses_taken += 1
        result.append(cur_course)
        if cur_course not in graph: continue
        for out in graph[cur_course]: 
            num_edges[out] -= 1

            if num_edges[out] == 0: 
                nodes.append(out)


    if courses_taken == numCourses: 
        return result
    return []

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
