from typing import * 

def solution(height: List[int]): 
    f_water = [0 for _ in range(len(height))]
    b_water = [0 for _ in range(len(height))]

    #forward loop 
    cur_max = 0
    for i in range(len(f_water)): 
        if height[i] > cur_max: 
            cur_max = height[i]
        else: 
            f_water[i] = cur_max - height[i]

    #backward loop 
    cur_max = 0
    for i in range(len(f_water)-1, -1, -1): 
        if height[i] > cur_max: 
            cur_max = height[i]
        else: 
            b_water[i] = cur_max - height[i]

    water = 0
    for i in range(len(f_water)): 
        water += min(f_water[i], b_water[i])

    return water


def test(solution: Callable[[List[int]], int]): 
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = solution(heights)
    print(sol)
    assert(sol == 6)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
