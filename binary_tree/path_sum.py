from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode], targetSum: int) -> bool: 

    def check_sum(root, t, c): 
        if not root: return False
        if not root.right and not root.right: 
            return t == (c + root.val)
        
        new_val = c+root.val
        return (check_sum(root.left, t, new_val) or 
                check_sum(root.right, t, new_val))

    return check_sum(root, targetSum, 0)

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
