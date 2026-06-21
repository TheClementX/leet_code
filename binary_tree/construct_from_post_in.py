from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]: 
    in_map = {val: idx for idx, val in enumerate(inorder)}

    def build(lo, hi, l_idx): 
        if lo > hi: return None, l_idx

        new_node = TreeNode(postorder[l_idx])
        mid = in_map[new_node.val]
        new_node.right, l_idx = build(mid+1, hi, l_idx-1)
        new_node.left, l_idx = build(lo, mid-1, l_idx)

        return new_node, l_idx

    root, _ = build(0, len(postorder)-1, len(postorder)-1)
    return root


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
