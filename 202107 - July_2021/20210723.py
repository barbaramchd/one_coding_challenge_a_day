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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        # check if we can prune the root
        if self.can_prune(root) == True:
            root = None

        return root

    # function that defines if we can prune a node
    def can_prune(self, node):
        # variable to check if we can prune left node
        left_child_check = True
        # variable to check if we can prune right node
        right_child_check = True

        if node.left:
            # if there is a left node, recursively calls function on the left node
            # and prune it
            left_child_check = self.can_prune(node.left)
            if left_child_check == True:
                node.left = None

        if node.right:
            # if there is a right node, recursively calls function on the right node
            # and prune it
            right_child_check = self.can_prune(node.right)
            if right_child_check == True:
                node.right = None

        if node.val == 0:
            # if node's value it 0 and both of its children can be pruned
            # we can also prune the node itself
            if left_child_check == True:
                if right_child_check == True:
                    return True
        return False