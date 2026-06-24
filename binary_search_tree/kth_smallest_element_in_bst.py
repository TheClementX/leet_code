from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode], k: int) -> int: 
    def listify(root): 
        if not root: return []
        return listify(root.left) + [root.val] + listify(root.right)
    
    vals = listify(root)
    return vals[k-1]

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
