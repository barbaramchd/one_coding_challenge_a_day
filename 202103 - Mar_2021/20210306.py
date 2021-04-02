"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
#SOLUTION 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

#SOLUTION 2
from functools import lru_cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def maxDepth(self, root: TreeNode) -> int:
        if root != None:
            if root.left != None and root.right != None:
                if self.maxDepth(root.left) > self.maxDepth(root.right):
                    return self.maxDepth(root.left) + 1
                else:
                    return self.maxDepth(root.right) + 1
            elif root.left != None and root.right == None:
                return self.maxDepth(root.left) + 1
            elif root.left == None and root.right != None:
                return self.maxDepth(root.right) + 1
            else:
                return 0 + 1
        return 0
