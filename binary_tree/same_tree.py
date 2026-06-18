from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool : 
    if not p and not q: return True
    p_val, q_val = None, None
    if p: p_val = p.val
    if q: q_val = q.val
    if p_val != q_val: return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
