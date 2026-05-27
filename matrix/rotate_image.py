from typing import * 

def solution(matrix: List[List[int]]) -> None: 
    top, bot, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    m, n = len(matrix)-1, len(matrix[0])-1

    while top < bot and left < right: 
        for c in range(left, right): 
            #offset gap to correct for a zero negative offset 
            g = n-right

            tmp1 = matrix[c][right]
            matrix[c][right] = matrix[top][c]

            tmp2 = matrix[bot][right-c+g]
            matrix[bot][right-c+g] = tmp1

            tmp3 = matrix[bot-c+g][left]
            matrix[bot-c+g][left] = tmp2

            matrix[top][c] = tmp3

        top += 1
        bot -= 1
        left += 1
        right -= 1



def test(solution: Callable[[List[List[int]]], None]): 
    matrix = [
        [1,2],
        [3,4]
    ]
    solution(matrix)
    print(matrix)
    assert(matrix == [[3,1], [4,2]])

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    solution(matrix)
    print(matrix)
    assert(matrix == [[7,4,1],[8,5,2],[9,6,3]])

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution(matrix)
    print(matrix)
    assert(matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
