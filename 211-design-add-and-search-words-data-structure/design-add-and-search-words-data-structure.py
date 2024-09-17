class TreeNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.endWord = True
            
    def search(self, word: str) -> bool:

        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):

                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]

            
            return curr.endWord
        return dfs(0, self.root)

                

        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)