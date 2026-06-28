from typing import * 
from collections import *

#O(n^2 * wordlen) solution
def solution(beginWord: str, endWord: str, wordList: list[str]) -> int: 
    def get_neighbors(word, word_list): 
        result = []
        for w in word_list: 
            dif = 0
            for i in range(len(word)): 
                if word[i] != w[i]: dif += 1
            if dif == 1: result.append(w)

        return result

    nodes, visited = deque([(beginWord, 1)]), set([beginWord])

    while nodes: 
        word, level = nodes.popleft()
        if word == endWord: return level 

        neighbors = get_neighbors(word, wordList)
        for word in neighbors: 
            if word not in visited: 
                visited.add(word)
                nodes.append((word, level+1))

    return 0

#much better runtime
#O(n * wordlen)
def solution(beginWord: str, endWord: str, wordList: list[str]) -> int: 
    def get_rungs(word): 
        letters = 'abcdefghijklmnopqrstuvwxyz'
        result = []

        for i in range(len(word)): 
            for l in letters: 
                if l != word[i]: 
                    result.append(word[:i] + l + word[i+1:])

        return result

    word_set = set(wordList)
    nodes, visited = deque([(beginWord, 1)]), set([beginWord])

    while nodes: 
        word, level = nodes.popleft()
        if word == endWord: return level 

        rungs = get_rungs(word)
        for r in rungs: 
            if r in word_set and r not in visited: 
                visited.add(r)
                nodes.append((r, level+1))

    return 0
        


def test(solution): 
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = solution(beginWord, endWord, wordList)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
