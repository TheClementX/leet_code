from typing import * 

def solution(ransomNote: str, magazine: str) -> bool: 
    counts = dict()
    for c in magazine: 
        counts[c] = counts.get(c, 0) + 1

    for c in ransomNote: 
        counts[c] = counts.get(c, 0) - 1
        if counts[c] < 0: 
            return False

    return True

def test(solution: Callable[[str, str], bool]): 
    ransomNote = 'a'
    magazine = 'b'
    assert(not solution(ransomNote, magazine))

    ransomNote = 'aa'
    magazine = 'ab'
    assert(not solution(ransomNote, magazine))

    ransomNote = 'aa'
    magazine = 'aab'
    assert(solution(ransomNote, magazine))
    
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
