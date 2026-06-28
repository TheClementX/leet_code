from typing import * 

class TrieNode: 
    def __init__(self, val=None, end=False): 
        self.val = val
        self.end = end
        self.neighbors = dict() 

class WordDictionary: 
    def __init__(self): 
        self.root = TrieNode()

    def addWord(self, word: str) -> None: 
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
        def get_word(node, word, i): 
            if i >= len(word): return node.end

            c = word[i]
            if c == '.': 
                for _, nbor in node.neighbors.items(): 
                    if get_word(nbor, word, i+1): return True
            elif c in node.neighbors: 
                if get_word(node.neighbors[c], word, i+1): 
                    return True

            return False

        return get_word(self.root, word, 0)

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
