from typing import * 

def solution(path: str) -> str: 
    dirs = path.split("/")
    result = []

    for i in range(len(dirs)): 
        if dirs[i] == "" or dirs[i] == ".": continue
        if dirs[i] == ".." and result: result.pop()
        elif dirs[i] == ".." and not result: continue
        else: result.append(dirs[i])

    return "/" + "/".join(result)

def test(solution: Callable[[str], str]): 
    path = "/home//foo/"
    sol = solution(path)
    print(sol)
    assert(sol == "/home/foo")

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
