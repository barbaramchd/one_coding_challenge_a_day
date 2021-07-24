"""
  Binary Tree Pruning

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if self.can_prune(root) == True:
            root = None

        return root

    def can_prune(self, node):
        left_child_check = True
        right_child_check = True

        if node.left:
            left_child_check = self.can_prune(node.left)
            if left_child_check == True:
                node.left = None

        if node.right:
            right_child_check = self.can_prune(node.right)
            if right_child_check == True:
                node.right = None

        if node.val == 0:
            if left_child_check == True:
                if right_child_check == True:
                    return True
        return False