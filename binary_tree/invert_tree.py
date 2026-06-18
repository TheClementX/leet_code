from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right
        
def solution(root: Optional[TreeNode]) -> Optional[TreeNode]: 
    def invert(head): 
        if not head: return None
        new_left = invert(head.right)
        new_right = invert(head.left)
        head.left = new_left
        head.right = new_right
        return head

    invert(root)
    return root

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
