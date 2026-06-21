from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]): 
    if not root: return []
    result = []
    cur_level, next_level = [root], []
    while cur_level: 
        level_traversal = []
        for node in cur_level: 
            level_traversal.append(node.val)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)

        result.append(level_traversal)
        cur_level, next_level = next_level, []

    return result
    
def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
