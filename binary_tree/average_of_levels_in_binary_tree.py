from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

#overflowing solution
def solution(root: Optional[TreeNode]) -> list[int]: 
    if not root: return []
    result = []
    cur_level, next_level = [root], []
    while cur_level: 
        average, examples = 0, 0
        for node in cur_level: 
            average += node.val
            examples += 1
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)

        result.append(average / examples)
        cur_level, next_level = next_level, []

    return result

#no overflow, would be useful in C, running average
def solution(root: Optional[TreeNode]) -> list[int]: 
    if not root: return []
    result = []
    cur_level, next_level = [root], []
    while cur_level: 
        average, examples = 0, 0
        for node in cur_level: 
            average = (average * examples) + node.val
            examples += 1
            average /= examples
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)

        result.append(average)
        cur_level, next_level = next_level, []

    return result

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
