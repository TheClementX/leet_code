from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

#stateless
def solution(inorder: list[int], preorder: list[int]) -> Optional[TreeNode]: 
    in_set = {val: i for i, val in enumerate(inorder)}
    p_idx = 0

    def build(lo, hi, mid): 
        if lo > hi: 
            return None, mid

        new = TreeNode(preorder[mid])
        i_idx = in_set[new.val]
        new.left, mid = build(lo, i_idx-1, mid+1)
        new.right, mid = build(i_idx+1, hi, mid)

        return new, mid

    root, _ = build(0, len(preorder)-1, p_idx)
    return root

#stateful
def solution(inorder: list[int], preorder: list[int]) -> Optional[TreeNode]: 
    in_set = {val: i for i, val in enumerate(inorder)}
        self.p_idx = 0

        def build(lo, hi): 
            if lo > hi: 
                return None

            new = TreeNode(preorder[self.p_idx])
            i_idx = in_set[new.val]
            self.p_idx += 1
            new.left = build(lo, i_idx-1)
            new.right = build(i_idx+1, hi)

            
            return new

        return build(0, len(inorder)-1)
def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
