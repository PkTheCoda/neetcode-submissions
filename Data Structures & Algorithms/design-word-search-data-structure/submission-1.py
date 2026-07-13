class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(index, node):
            if index == len(word):
                return node.endOfWord
                

            
            if word[index] == ".":
                for char in node.children:
                    if dfs(index + 1, node.children[char]):
                        return True
                
                return False
            elif word[index] in node.children:
                return dfs(index + 1, node.children[word[index]])
            else:
                return False

            
        
        return dfs(0, curr)
