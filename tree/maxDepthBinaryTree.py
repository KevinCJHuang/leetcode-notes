# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: recursion
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
#         # Approach 2: DFS
#         if not root:
#             return 0
        
#         maxDepth = 1
#         stack = [(root, 1)]
#         while len(stack):
#             node = stack.pop()
#             maxDepth = max(maxDepth, node[1])
#             if (node[0].left):
#                 stack.append((node[0].left, node[1] + 1))
#             if (node[0].right):
#                 stack.append((node[0].right, node[1] + 1))
#         return maxDepth