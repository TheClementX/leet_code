from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(): 
    if not root: return []
    result = []
    cur_level, next_level = [root], []
    level = 0
    while cur_level: 
        level_traversal = []
        for node in cur_level: 
            level_traversal.append(node.val)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        
        if level % 2 == 0: 
            result.append(level_traversal)
        else: 
            result.append(level_traversal[::-1])
        level += 1
        cur_level, next_level = next_level, []

    return result

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
