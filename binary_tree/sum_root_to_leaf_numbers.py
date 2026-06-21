from typing import * 

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]) -> int: 
    def get_numbers(root, n, nums): 
        if not root: return nums
        n = (n * 10) + root.val

        nums = get_numbers(root.left, n, nums)
        nums = get_numbers(root.right, n, nums)

        if not root.left and not root.right: 
            nums.append(n)

        return nums

    return sum(get_numbers(root, 0, []))

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
