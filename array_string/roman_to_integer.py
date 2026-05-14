from typing import * 

def solution(s: str) -> int: 
    def get_val(s: str) -> int: 
        match s: 
            case 'I': return 1
            case 'V': return 5
            case 'X': return 10
            case 'L': return 50 
            case 'C': return 100
            case 'D': return 500
            case 'M': return 1000

    val, i = 0, 0
    while i < len(s):
        print(i)
        cv = get_val(s[i])
        nv = 0 if i == len(s)-1 else get_val(s[i+1]) 

        if cv < nv: 
            val += nv - cv
            i += 1 
        else: 
            val += cv
        i += 1

    return val

def solution(s: str) -> int: 
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for i in range(len(s)): 
        if i < len(s)-1 and s[i] < s[i+1]:
            val -= roman[s[i]]
        else:
            val += roman[s[i]]

    return val



def test(solution: Callable[[str],int]): 
    num = "III"
    sol = solution(num)
    print(sol)
    assert(sol == 3)

    num = "IV"
    sol = solution(num)
    print(sol)
    assert(sol == 4)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
