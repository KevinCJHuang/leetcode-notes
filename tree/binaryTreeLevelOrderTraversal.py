# Binary Tree Level Order Traversal https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = [(root, 0)]
        while len(q):
            node = q.pop(0)
            if not node[0]:
                continue
            if len(arr) == node[1]:
                arr.append([])
            arr[node[1]].append(node[0].val)
            q.append((node[0].left, node[1] + 1))
            q.append((node[0].right, node[1] + 1))
        return arr
