from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        cur_p = root
        while cur_p: 
            self.stack.append(cur_p)
            cur_p = cur_p.left

    def next(self) -> int:
        cur_node = self.stack.pop()
        if cur_node.right: 
            cur_p = cur_node.right
            while cur_p: 
                self.stack.append(cur_p)
                cur_p = cur_p.left

        return cur_node.val

    def hasNext(self) -> bool:
        return self.stack != []

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
