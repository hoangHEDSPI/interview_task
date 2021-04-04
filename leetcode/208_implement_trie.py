import collections


class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self._is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_root = self.root
        for c in word:
            current_root = current_root.children[c]
        current_root._is_word = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_root = self.root
        for c in word:
            current_root = current_root.children.get(c)
            if current_root is None:
                return False
        return current_root._is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_root = self.root
        for c in prefix:
            current_root = current_root.children.get(c)
            if current_root is None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)