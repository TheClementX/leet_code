from typing import * 

def solution(strs: List[str]) -> str: 
    def ordered_intersection(s1, s2): 
        result = ''
        for i in range(len(s1)): 
            if s1[i] == s2[i]: 
                result += s1[i]
            else:
                return result
        return result

    s_strs = sorted(strs, key=len)
    shortest = s_strs[0]
    for i in range(1, len(s_strs)): 
        shortest = ordered_intersection(shortest, s_strs[i])

    return shortest

def test(solution: Callable[[List[str]], int]): 
    strs = ['race', 'racecar', 'racewar', 'racer']
    sol = solution(strs)
    print(sol)
    assert(sol == 'race')

    strs = ['flower', 'flow', 'flight']
    sol = solution(strs)
    print(sol)
    assert(sol == 'fl')

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
