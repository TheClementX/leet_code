from typing import * 

class Node: 
    def __init__(self, val=0, neighbors=None): 
        self.val = val
        self.neighbors = neighbors

def solution(self, node: Optional[Node]) -> Optional[Node]: 
    if not node: return None

    def clone(node, visited): 
        if node in visited: return visited[node]

        new_node = Node(node.val, [])
        visited[node] = new_node

        for nbor in node.neighbors: 
            clone_nbor = clone(nbor, visited)
            new_node.neighbors.append(clone_nbor)

        return new_node

    return clone(node, dict())

#iterative BFS
def solution(self, node: Optional[Node]) -> Optional[Node]: 
    if not node: return None

    nodes, clones = deque([node]), {node: Node(val=node.val, neighbors=[])}

    while nodes: 
        cur = nodes.popleft()

        for nbor in cur.neighbors:
            if nbor not in clones: 
                clones[nbor] = Node(val=nbor.val, neighbors=[])
                nodes.append(nbor)

            clones[cur].neighbors.append(clones[nbor])

    return clones[node]


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
