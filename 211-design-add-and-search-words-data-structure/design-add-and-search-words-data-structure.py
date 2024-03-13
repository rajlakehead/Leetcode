class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes mapped by characters
        self.children = {}  
        # Flag indicating whether the node represents the end of a word
        self.isWord = False  


class WordDictionary:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            # Create a new node if the child does not exist
            if w not in curr.children:
                curr.children[w] = TrieNode()  
            curr = curr.children[w]
        # Mark the last node as representing the end of the inserted word
        curr.isWord = True  

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                w = word[i]
                # Handle wildcard character "."
                if w == ".":  
                    # Recursively search all child nodes for wildcard query
                    for child in curr.children.values():  
                        if dfs(i + 1, child):  
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            # Return True if the last node represents the end of a word
            return curr.isWord  

        # Start DFS search from the root
        return dfs(0, self.root)  