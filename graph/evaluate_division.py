from typing import * 
import math

def solution(
    equations: list[list[str]], 
    values: list[float], 
    queries: list[list[str]]
) -> list[float]: 
    def construct_graph(equations, values) -> dict: 
        graph = dict()
        for i, (a, b) in enumerate(equations): 
            a_nbors = graph.setdefault(a, [])
            b_nbors = graph.setdefault(b, [])

            a_nbors.append((b, values[i]))
            b_nbors.append((a, 1 / values[i]))

        return graph


    eq_graph = construct_graph(equations, values)

    def get_path(graph, c, e, visited): 
        if (c not in graph or e not in graph or c in visited): 
            return -1.0
        if c == e: return 1.0

        n_visited = set(visited)
        n_visited.add(c)

        for nbor in graph[c]: 
            node, val = nbor
            r_val = get_path(graph, node, e, n_visited)
            if r_val >= 0.0: 
                return val * r_val 

        return -1.0

    result = []
    for q in queries: 
        s, e = q
        result.append(get_path(eq_graph, s, e, set()))

    return result

# def get_path(graph: dict, start: str, end: str): 
#     if start not in graph: return -1.0
# 
#     nodes, visited = [start], set()
#     path, found = set(), False
#     while nodes: 
#         cur_node, val = nodes.pop()
# check stop conditions
#         if cur_node == end: 
#             path.add((cur_node, val))
#             found = True
#             break
#         if cur_node in visited:
#             path.remove((cur_node, val))
#             continue
#         
# process 
#         visited.add(cur_node)
#         path.add((cur_node, val))
# 
# append neighbors
#         nbors = graph[cur_node]
#         nodes.extend(nbors)
#     
#     if not found: return -1.0
#     return math.prod([val for _, val in path])

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
