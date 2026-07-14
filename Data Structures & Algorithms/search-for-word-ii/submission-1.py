class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        res = []

        root = TrieNode()

        # add each word in
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        def dfs(row, col, seen, node):
            if node.word:
                res.append(node.word)
                node.word = None
            
            
            # keep going because word might be in word
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in seen or board[row][col] not in node.children:
                return
            
            curr_char = board[row][col]

            seen.add((row, col))
            dfs(row + 1, col, seen, node.children[curr_char])
            dfs(row - 1, col, seen, node.children[curr_char])
            dfs(row, col + 1, seen, node.children[curr_char])
            dfs(row, col - 1, seen, node.children[curr_char])
            seen.discard((row, col))

        
        for row in range(len(board)):
            for col in range(len(board[row])):
                dfs(row, col, set(), root)

        return res