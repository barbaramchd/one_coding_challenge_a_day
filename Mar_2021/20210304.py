"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_level_symmetric(lst):
    for i in range(len(lst) // 2):
        if lst[i].val != lst[-i - 1].val:
            return False
    return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        children = [root]

        while True:
            children2 = []
            has_children = False
            for child in range(len(children)):
                if children[child].left:
                    children2.append(children[child].left)
                    has_children = True
                else:
                    children2.append(TreeNode(val="😎"))

                if children[child].right:
                    children2.append(children[child].right)
                    has_children = True
                else:
                    children2.append(TreeNode(val="😎"))

            # print(is_level_symmetric(children2))

            if is_level_symmetric(children2) == False:
                return False
            if has_children == False:
                return True
            else:
                children = []
                for c in range(len(children2)):
                    if children2[c].val != "😎":
                        children.append(children2[c])
                children2 = []


