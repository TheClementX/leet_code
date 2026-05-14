from typing import * 

def solution(s: str) -> str: 
    words = s.strip().split(" ")
    rev = []
    for i in range(len(words)): 
        if words[i] != '': 
            rev.append(words[i].strip())

    rev = rev[::-1]
    return " ".join(rev)

def test(solution: Callable[[str], str]): 
    s = "   the sky  is blue  "
    sol = solution(s)
    print(sol)
    assert(sol == "blue is sky the")
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
