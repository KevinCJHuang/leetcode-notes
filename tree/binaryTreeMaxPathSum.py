# 124. Binary Tree Maximum Path Sum https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode]) -> (int, int): # max, left + me or right + me
        if not root:
            return (float('-inf'), float('-inf'), float('-inf'))
        leftResult = self.helper(root.left)
        rightResult = self.helper(root.right)

        includeMeUsable = max(leftResult[1] + root.val, rightResult[1] + root.val, root.val)
        curMax = max(leftResult[0], rightResult[0], leftResult[1] + rightResult[1] + root.val, includeMeUsable)
        return (curMax, includeMeUsable)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]
