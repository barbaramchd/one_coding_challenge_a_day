"""
Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = self.depth_counter(root)

        return self.deepest_leaves(root, max_depth)

    def depth_counter(self, node):
        if node.left:
            left = self.depth_counter(node.left)
        else:
            left = 0

        if node.right:
            right = self.depth_counter(node.right)
        else:
            right = 0

        return max(left, right) + 1

    def deepest_leaves(self, node, max_depth):
        if node.left:
            left = self.deepest_leaves(node.left, max_depth - 1)
        else:
            left = 0

        if node.right:
            right = self.deepest_leaves(node.right, max_depth - 1)
        else:
            right = 0

        if max_depth == 1:
            return node.val

        return sum([left, right])
