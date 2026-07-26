from typing import * 

def solution(self, s: str, wordDict: List[str]) -> bool:
    def word_break(s, wordDict, cache): 
        if s == "": return True

        solvable = False
        for word in wordDict: 
            if s.startswith(word): 
                next_s = s[len(word):]
                if next_s not in cache: 
                    cache[next_s] = word_break(next_s, wordDict, cache)
                solvable = solvable or cache[next_s]

        return solvable

    return word_break(s, wordDict, dict())

def solution(s: str, wordDict: list[str]) -> bool: 
    word_set = set(wordDict)

    cache = [False] * (len(s) + 1)
    cache[0] = True

    for i in range(1, len(s)+1): 
        for j in range(i): 
            if cache[j] and s[j:i] in word_set: 
                cache[i] = True
                break

    return cache[len(s)]


def test(solution): 
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = solution(s, wordDict)
    print(sol)
    assert(sol == True)

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    sol = solution(s, wordDict)
    print(sol)
    assert(sol == True)

    s = "catsandog" 
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = solution(s, wordDict)
    print(sol)
    assert(sol == False)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
