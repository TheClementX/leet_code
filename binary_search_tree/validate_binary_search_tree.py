from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]): 
    def validate(root, lbound, rbound): 
        if not root: return True
        if root.val >= rbound or root.val <= lbound: 
            return False

        return (validate(root.left, lbound, root.val) and
                validate(root.right, root.val, rbound))

    return validate(root, float('-inf'), float('inf'))

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
