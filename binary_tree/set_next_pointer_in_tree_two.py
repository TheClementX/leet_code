from typing import * 

class Node(): 
    def __init__(self, val=0, left=None, right=None, next=None): 
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#O(n) space
def solution(root: Optional[Node]) -> Optional[Node]: 
    if not root: return None

    cur, next = [root], []
    while cur: 
        for i in range(len(cur)): 
            c_node = cur[i]
            if i < len(cur)-1: 
                c_node.next = cur[i+1]
            if c_node.left: next.append(c_node.left)
            if c_node.right: next.append(c_node.right)

        cur, next = next, []

    return root
        
#O(1) space
def solution(root: Optional[Node]) -> Optional[Node]: 
    if not root: return None

    list_head = root
    while list_head: 
        cur_p = list_head
        first, nodes = None, []
        while cur_p: 
            if cur_p.left: nodes.append(cur_p.left)
            if cur_p.right: nodes.append(cur_p.right)
            if not first and nodes: first = nodes[0]
            
            if len(nodes) > 1: 
                for i in range(len(nodes)): 
                    if i < len(nodes)-1: 
                        nodes[i].next = nodes[i+1]
                last = nodes[-1]
                nodes = [last]
            cur_p = cur_p.next

        list_head = first
    return root

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
