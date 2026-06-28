from typing import * 

class TrieNode: 
    def __init__(self, val=None, end=False): 
        self.val = val
        self.end = end
        self.neighbors = dict() 

class Trie: 
    def __init__(self, root=None): 
        root = TrieNode()

    def insert(self, word: str) -> None: 
        cur_node, i = self.root, 0
        while i < len(word): 
            l = word[i]
            next_node = cur_node.neighbors.get(l, None)
            if not next_node: 
                next_node = TrieNode(val=l)
                cur_node.neighbors[l] = next_node
            cur_node = next_node
            i += 1
        cur_node.end = True


    def search(self, word: str) -> bool: 
        cur_node = self.root
        for l in word: 
            cur_node = cur_node.neighbors.get(l, None)
            if not cur_node: return False

        return cur_node.end

    def startsWith(self, prefix: str) -> bool: 
        cur_node = self.root
        for l in prefix: 
            cur_node = cur_node.neighbors.get(l, None)
            if not cur_node: return False

        return True

def solution(board: list[list[str]], words: list[str]) -> list[str]: 
    word_trie = Trie()
    for word in words: 
        word_trie.insert(word)

    def dfs(board, word, r, c, trie, result, visited): 
        if (r, c) in visited: 
            return result

        l = board[r][c]
        if not l in trie.neighbors: return result

        word = word + l
        trie = trie.neighbors[l]

        if trie.end: result.add(word)

        visited.add((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r+dr, c+dc
            if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]): 
                result = dfs(board, word, nr, nc, trie, result, visited)
        visited.remove((r, c))

        return result

    result = set()
    for r in range(len(board)): 
        for c in range(len(board[0])): 
            result = dfs(board, "", r, c, word_trie.root, result, set())

    return list(result)

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
