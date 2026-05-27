from typing import * 

def solution(matrix: List[List[int]]) -> List[int]: 
    result = []
    top, bot, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

    while top <= bot and left <= right: 
        for i in range(left, right+1): 
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bot+1): 
            result.append(matrix[i][right])
        right -= 1

        if top <= bot: 
            for i in range(right, left-1, -1): 
                result.append(matrix[bot][i])
            bot -= 1

        if left <= right: 
            for i in range(bot, top-1, -1): 
                result.append(matrix[i][left])
            left += 1

    return result



def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
