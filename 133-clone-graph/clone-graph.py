"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newnode = Node(node.val)
            oldToNew[node] = newnode

            for n in node.neighbors:
                oldToNew[node].neighbors.append(dfs(n))

            return newnode

        return dfs(node) if node else None

