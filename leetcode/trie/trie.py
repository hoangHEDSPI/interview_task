from typing import List, Tuple


class TrieNode:
    """A node in the trie structure."""
    def __init__(self, char) -> None:
        # the character stored in this node
        self.char = char
        # whether this can be the end of a word
        self.is_end = False
        # a counter indicating how many times a word is inserted
        self.counter = 0

        # a dictionary of child nodes 
        # keys are characters, values are nodes
        self.children = {}

class Trie(object):
    """The trie object."""
    def __init__(self) -> None:
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        super().__init__()
        self.root = TrieNode("")
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root

        # Loop through each character in the word
        # check if there is no child containing the character, create a new child for
        # the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found
                # create a new node in the trie
                new_node = TrieNode(char=char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of the word
        node.is_end = True

        # Increase the counter to indicate that we see this word once more
        node.counter += 1
    
    def dfs(self, node: TrieNode, prefix: str) -> List[Tuple(str, int)]:
        """Depth-first search of the trie.
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a word while traversing the trie
        """
        # self.output: List[Tuple(str, int)] = []
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in the trie starting
        with this prefix, sorts the words by the number of times they have been inserted.
        Args:
            - x: prefix query
        """
        self.output = []
        node = self.node

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)