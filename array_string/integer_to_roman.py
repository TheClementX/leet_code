from typing import * 

def solution(num: int) -> str: 
    roman = {
        1000: 'M', 
        900: 'CM', 500: 'D', 400: 'CD',   
        100: 'C', 90: 'XC', 50: 'L', 
        40: 'XL', 10: 'X', 9: 'IX', 
        5: 'V', 4: 'IV', 1: 'I'
    }

    res = ''
    for key, val in roman.items(): 
        if num == 0: 
            return res

        count, num = divmod(num, key)
        res += (val * count)

    return res
        

def test(solution: Callable[[int], str]): 
    val = 3749
    sol = solution(val)
    print(sol)
    assert(sol == "MMMDCCXLIX")
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
