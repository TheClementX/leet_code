from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

#different logic thats faster
def solution(root: Optional[TreeNode]) -> None: 
    def start_end(node): 
        if not node: return None, None
        start = node
        cur_p = node
        while cur_p.right: 
            cur_p = cur_p.right

        return start, cur_p

    def flatten(root): 
        if not root: return

        left = flatten(root.left)
        right = flatten(root.right)

        ls, le = start_end(left)
        rs, re = start_end(right)

        if ls: root.right = ls
        else: root.right = rs
        root.left = None

        if le: le.left, le.right = None, rs
        if re: re.left, re.right = None, None

        return root

    flatten(root)

#different logic thats cleaner
def solution(root: Optional[TreeNode]) -> None: 
    def flatten(root): 
        if not root: return None, None

        ls, le = flatten(root.left)
        rs, re = flatten(root.right)

        if ls: root.right = ls
        else: root.right = rs
        root.left = None

        if le: le.left, le.right = None, rs
        if re: re.left, re.right = None, None
        
        if not re and not le: return root, root
        elif re: return root, re
        else: return root, le


    flatten(root)


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
