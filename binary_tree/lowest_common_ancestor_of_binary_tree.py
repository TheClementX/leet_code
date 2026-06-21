from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

#brute force too slow
def solution(
    root: Optional[TreeNode], 
    p: Optional[TreeNode], 
    q: Optional[TreeNode]
) -> Optional[TreeNode]: 

    def lca(root, p, q): 
        if not root or root == p or root == q: return root

        left = lca(root.left, p, q)
        right = lca(root.right, p, q)

        if left and right: 
            return root

        return left if left else right

    return lca(root, p, q)

def solution(
    root: Optional[TreeNode], 
    p: Optional[TreeNode], 
    q: Optional[TreeNode]
) -> Optional[TreeNode]: 
    def contains(root, t): 
        if not root: return False
        if root is t: return True
        return contains(root.right, t) or contains(root.left, t)

    def lca(root, p, q): 
        if not root: return None

        pl, pr = contains(root.left, p), contains(root.right, p)
        ql, qr = contains(root.left, q), contains(root.right, q)

        if pl and ql: return lca(root.left, p, q)
        elif pr and qr: return lca(root.right, p, q)
        else: return root

    return lca(root, p, q)

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
