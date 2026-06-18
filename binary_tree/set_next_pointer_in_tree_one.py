from typing import * 

class Node(): 
    def __init__(self, val=0, left=None, right=None, next=None): 
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def solution(root: Optional[Node]) -> Optional[Node]: 
    if not root: return None
    
    def set_nexts(left, right): 
        nodes = []
        if left and left.left: nodes.append(left.left)
        if left and left.right: nodes.append(left.right)
        if right and right.left: nodes.append(right.left)
        if right and right.right: nodes.append(right.right)

        if not nodes: return 

        if len(nodes) == 1: 
            set_nexts(None, nodes[0])
        else: 
            for i in range(len(nodes)): 
                if i < len(nodes)-1: 
                    nodes[i].next = nodes[i+1]
                    set_nexts(nodes[i], nodes[i+1])
    
    if root.left and root.right: 
        root.left.next = root.right
    set_nexts(root.left, root.right)
    return root





def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
