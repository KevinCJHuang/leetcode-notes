# 133. Clone Graph https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        q = deque([node])
        m = {}
        visited = set()

        while q:
            oldNode = q.pop()
            if oldNode in visited:
                continue
            else:
                visited.add(oldNode)
            
            if oldNode not in m:
                m[oldNode] = Node(oldNode.val)

            for neigh in oldNode.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[oldNode].neighbors.append(m[neigh])
                q.append(neigh)

        return m[node]
