from typing import * 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(nums: list[int]) -> Optional[TreeNode]: 
    def create_tree(lo, hi, nums): 
        if lo > hi: 
            return None

        mid = lo + ((hi - lo) // 2)

        root = TreeNode(nums[mid])
        root.left = create_tree(lo, mid-1, nums)
        root.right = create_tree(mid+1, hi, nums)

        return root

    return create_tree(0, len(nums)-1, nums)


def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
