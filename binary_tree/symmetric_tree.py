from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]) -> bool: 
    if not root: return True

    def symmetric(node1, node2): 
        if not node1 and not node2: 
            return True
        if node1 and node2: 
            return (node1.val == node2.val and
                    symmetric(node1.left, node2.right) and
                    symmetric(node1.right, node2.left))
        elif node1 or node2: 
            return False

    return symmetric(root.left, root.right)
    

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
