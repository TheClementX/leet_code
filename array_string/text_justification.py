import math
from typing import * 

def solution(words: List[str], maxWidth: int) -> List[str]: 
    result = []
    cur_words = []
    cur_chars = 0

    for word in words: 
        #if cannot add next word justify and reset
        if len(cur_words) + cur_chars + len(word) > maxWidth: 
            spaces = maxWidth - len("".join(cur_words))
            #round robbin asign spaces
            if len(cur_words) != 1: 
                for i in range(spaces): 
                    idx = i % (len(cur_words)-1)
                    cur_words[idx] += " "
            else: 
                cur_words[0] += (" " * spaces)
                
            result.append("".join(cur_words))
            cur_words = []
            cur_chars = 0

        #always append words, notice this means 
        #we will always handle the last line seperately
        cur_words.append(word)
        cur_chars += len(word)

    last_line = " ".join(cur_words)
    result.append(last_line.ljust(maxWidth))

    return result

"""
this is my first attempt it does not work due to some off by one errors
"""
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    def join_add_spaces(w, width): 
        result = ''
        spaces = width - len("".join(w))
        if(len(w) == 1): return w[0] + (" " * spaces)
        spaces_per = math.ceil(spaces/(len(w) - 1))

        for i in range(len(w)-1): 
            result += w[i]
            spaces_per = spaces_per if spaces_per <= spaces else spaces
            result += (" " * spaces_per)
            spaces -= spaces_per

        result += w[-1]
        return result

    result = []
    cur_words = []
    cur_length = 0
    for i in range(len(words)): 
        min_len = len(words[i]) + 1
        if cur_length + min_len < maxWidth: 
            cur_words.append(words[i])
            cur_length += min_len
        elif cur_length + min_len == maxWidth: 
            cur_words.append(words[i])
            result.append(join_add_spaces(cur_words, maxWidth))
            cur_words, cur_length = [], 0
        else:
            result.append(join_add_spaces(cur_words, maxWidth))
            cur_words, cur_length = [words[i]], min_len
    result.append(join_add_spaces(cur_words, maxWidth))

    #left justify final line
    last_line = result[-1]
    last_line = last_line.split()
    last_line = " ".join(last_line)
    spaces = maxWidth - len(last_line)
    result[-1] = last_line + (" " * spaces)

    return result


def test(solution: Callable[[List[str], int], List[str]]): 
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    sol = solution(words, maxWidth)
    print(sol)
    ref_sol = [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]

    assert(sol == ref_sol)

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    sol = solution(words, maxWidth)
    print(sol)
    ref_sol = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]

    assert(sol == ref_sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
