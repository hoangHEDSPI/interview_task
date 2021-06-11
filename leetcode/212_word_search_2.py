from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self._is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current_root = self.root
        for c in word:
            current_root = current_root.children[c]
        current_root._is_word = True
                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)
        node = trie.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, "", res)
        return res
    
    def dfs(self, board: List[List[str]], i: int, j: int, node: TrieNode, path: List[str], res: List[str]):
        if node._is_word:
            res.append(path)
            node._is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, i+1, j, node, path+tmp, res)
        self.dfs(board, i-1, j, node, path+tmp, res)
        self.dfs(board, i, j+1, node, path+tmp, res)
        self.dfs(board, i, j-1, node, path+tmp, res)
        board[i][j] = tmp

if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    sol = Solution()
    assert set(sol.findWords(board, words)) == set(["eat","oath"])
