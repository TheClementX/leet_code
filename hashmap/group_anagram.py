from typing import * 

def solution(strs: List[str])-> List[List[str]]: 
    ana_map = dict()

    def create_freq_map(s): 
        freq_map = dict()
        for c in s: 
            freq_map[c] = freq_map.get(c, 0) + 1
        return freq_map

    for word in strs: 
        freq_map = create_freq_map(word) 
        key = tuple(sorted([(k, v) for k, v in freq_map.items()], key=lambda x: x[0]))
        #append modifies in place
        ana_map.setdefault(key, []).append(word)

    return [val for key, val in ana_map.items()]

def test(solution: Callable[[List[str]], List[List[str]]]): 
    strs = ["eat","tea","tan","ate","nat","bat"]
    target = [["bat"],["nat","tan"],["ate","eat","tea"]]
    sol = solution(strs)
    print(sol)
    assert(sol == target)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
