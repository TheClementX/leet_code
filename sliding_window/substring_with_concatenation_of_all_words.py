from typing import * 

def solution(s: str, words: List[str]) -> List[int]: 
    word_counts, word_set, result = dict(), set(words), []
    for word in words: 
        word_counts[word] = word_counts.get(word, 0) + 1

    word_len = len(words[0])

    for o in range(word_len): 
        #for each offset solve a sliding window problem
        lo, cur_counts = o, dict()
        for hi in range(o, len(s), word_len): 
            if hi+word_len > len(s): break
            word = s[hi:hi+word_len]

            #check if word is valid
            if word not in word_set: 
                lo, cur_counts = hi + word_len, dict()
                continue

            #check if counts is too large and shrink window
            cur_counts[word] = cur_counts.get(word, 0) + 1
            while cur_counts[word] > word_counts[word]: 
                lo_word = s[lo:lo+word_len]
                cur_counts[lo_word] = cur_counts.get(lo_word, 0)-1
                lo += word_len

            #check if a substring has been found
            print(lo, hi)
            if cur_counts == word_counts: 
                result.append(lo)

    return result

def test(solution: Callable[[str, List[str]], List[int]]): 
    s = 'barfoothefoobarman'
    words = ['bar', 'foo']
    sol = solution(s, words)
    print(sol)
    assert(sol == [0,9])
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
