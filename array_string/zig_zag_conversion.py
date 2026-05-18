from typing import * 

def solution(s: str, numRows: int) -> str: 
    if len(s) <= numRows or numRows == 1: 
        return s

    zigzag = ''
    for i in range(numRows): 
        if i == 0 or i == (numRows-1): 
            pos = i
            while pos < len(s): 
                zigzag += s[pos]
                pos += ((numRows * 2) - 2)
        else: 
            pos = i 
            pos_t = i + (2*(numRows-2) - (2*(i-1)))

            while pos < len(s): 
                zigzag += s[pos]
                pos += ((numRows * 2) - 2)
                if pos_t < len(s): 
                    zigzag += s[pos_t]
                    pos_t += ((numRows * 2) - 2)

    return zigzag

def solution2(s: str, numRows: int) -> str
    """
    simulate the rows by going up and down
    """


def test(solution: Callable[[str, int], str]): 
    s = "IWANTTOLIVEABIGAWESOMELIFE"
    numrows = 6
    sol = solution(s, numrows)
    print(sol)
    assert(sol == "IEMWVAOEAIBSLNLIEITOGWFTAE")

    s = "PAYPALISHIRING"
    numrows = 3
    sol = solution(s, numrows)
    print(sol)
    assert(sol == "PAHNAPLSIIGYIR")

    s = "AB"
    numrows = 1
    sol = solution(s, numrows)
    print(sol)
    assert(sol == "AB")

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
