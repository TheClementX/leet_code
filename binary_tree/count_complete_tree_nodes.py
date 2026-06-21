from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]): 
    if not root: return 0
    def get_height(root): 
        if not root: return 0
        l_height, r_height = 1, 1
        lp, rp = root.left, root.right
        while lp or rp: 
            if lp: 
                lp = lp.left
                l_height += 1
            if rp: 
                rp = rp.right
                r_height += 1

        if l_height == r_height: 
            return (2 ** l_height)-1

        return 1 + get_height(root.left) + get_height(root.right)
    
    return 1 + get_height(root.left) + get_height(root.right)


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
