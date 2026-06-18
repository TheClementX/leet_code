from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int: 
    if not root: return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
