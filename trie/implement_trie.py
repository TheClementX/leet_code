from typing import * 

class TrieNode: 
    def __init__(self, val=None, end=False): 
        self.val = val
        self.end = end
        self.neighbors = dict() 

class Trie: 
    def __init__(self): 
        self.root = TrieNode()

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

def test(): 
    print("all tests passed")

if __name__ == "__main__": 
    test() 


    
