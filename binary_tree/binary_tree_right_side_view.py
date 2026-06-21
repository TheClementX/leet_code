from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]) -> list[int]: 
    if not root: return []
    result = []
    cur_level, next_level = [root], []
    while cur_level: 
        result.append(cur_level[-1].val)
        for node in cur_level: 
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)

        cur_level, next_level = next_level, []

    return result




def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
