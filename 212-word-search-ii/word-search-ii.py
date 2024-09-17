class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(row, col, parent, word_path):
            letter = board[row][col]
            curr_node = parent.children[letter]

            word_path += letter
            if curr_node.is_end_of_word:
                result.add(word_path)
                curr_node.is_end_of_word = False  # Avoid duplicate results

            board[row][col] = '#'  # Mark cell as visited
            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + row_offset, col + col_offset
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if board[new_row][new_col] in curr_node.children:
                        backtrack(new_row, new_col, curr_node, word_path)

            board[row][col] = letter  # Restore the cell

            if not curr_node.children:
                parent.children.pop(letter)

        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root, "")

        return list(result)