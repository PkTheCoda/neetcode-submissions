class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # insert "bad"
        curr = self.root
        for char in word:

            # char doesnt exist, add it to children of curr (root)
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # always branch into next char.
            curr = curr.children[char]
        
        # mark that this is the end of a word
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True
        
        