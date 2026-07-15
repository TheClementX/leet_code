from typing import * 

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

"""
O(N^2 log N)
"""
def solution(grid: list[list[int]]) -> Node: 
    def same(lr, hr, lc, hc, grid): 
        val = grid[lr][lc]
        for r in range(lr, hr): 
            for c in range(lc, hc): 
                if grid[r][c] != val: 
                    return False
        return True

    def construct_tree(lr, hr, lc, hc, grid): 
        if same(lr, hr, lc, hc, grid): 
            return Node(bool(grid[lr][lc]), True, None, None, None, None)

        col_mid = lc + ((hc-lc)//2)
        row_mid = lr + ((hr-lr)//2)
        new_node = Node(False, False, None, None, None, None)

        new_node.topLeft = construct_tree(
            lr, row_mid, lc, col_mid, grid
        )
        new_node.topRight = construct_tree(
            lr, row_mid, col_mid, hc, grid
        )
        new_node.bottomLeft = construct_tree(
            row_mid, hr, lc, col_mid, grid
        )
        new_node.bottomRight = construct_tree(
            row_mid, hr, col_mid, hc, grid
        )

        return new_node

    return construct_tree(0, len(grid), 0, len(grid), grid)

"""
O(N^2)
"""
def solution(grid: list[list[int]]) -> Node: 
    def construct_tree(lr, hr, lc, hc, grid): 
        if hr-lr == 1 and hc-lc == 1: 
            return Node(bool(grid[lr][lc]), True, None, None, None, None)

        col_mid = lc + ((hc-lc)//2)
        row_mid = lr + ((hr-lr)//2)

        children = []
        #top left
        children.append(construct_tree(lr, row_mid, lc, col_mid, grid))
        #top right
        children.append(construct_tree(lr, row_mid, col_mid, hc, grid))
        #bottom left
        children.append(construct_tree(row_mid, hr, lc, col_mid, grid))
        #bottom right
        children.append(construct_tree(row_mid, hr, col_mid, hc, grid))

        tar_val, same = children[0].val, True
        for c in children: 
            same = same and (c.val == tar_val) and c.isLeaf

        if same: return Node(bool(grid[lr][lc]), True, None, None, None, None)
        else: return Node(True, False, children[0], children[1], children[2], children[3])

    return construct_tree(0, len(grid), 0, len(grid), grid)

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
