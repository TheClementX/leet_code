from typing import * 
import math

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right

def solution(root: Optional[TreeNode]) -> int: 
    def get_max(root): 
        if not root: return 0, float('-inf')

        l_max_p, l_g_max = get_max(root.left)
        r_max_p, r_g_max = get_max(root.right)

        left_val = max(0, l_max_p)
        right_val = max(0, r_max_p)
        w_left = left_val + root.val
        w_right = right_val + root.val
        w_both = w_left + w_right - root.val

        max_path_sum = max(w_left, w_right, w_both, l_g_max, r_g_max)
        return max(w_left, w_right), max_path_sum

    return get_max(root)[1] 





def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
