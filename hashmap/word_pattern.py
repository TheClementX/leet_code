from typing import * 

def solution(pattern: str, s: str) -> bool: 
    wl = s.split(" ")
    if len(wl) != len(pattern): return False

    p_map = dict() #map pattern letters to words
    w_map = dict() #map words to pattern letters
    for i in range(len(pattern)): 
        c, w = pattern[i], wl[i]
        p_map_val = p_map.get(c, -1)
        w_map_val = w_map.get(w, -1)
        if p_map_val == -1 and w_map_val == -1: 
            p_map[c], w_map[w] = w, c
        elif p_map_val != w or w_map_val != c: 
            return False #must check forward and backward mapping

    return True

def test(solution: Callable[[str, str], bool] ): 
    pattern = 'abba'
    s = 'dog cat cat dog'
    assert(solution(pattern, s))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
