"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, n: Optional['Node']) -> Optional['Node']:
        copy = {}
        
        def dfs(node):
            if node in copy:
                return copy[node]

            newnode = Node(node.val)
            copy[node] = newnode

            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            
            return newnode
        
        return dfs(n) if n else None