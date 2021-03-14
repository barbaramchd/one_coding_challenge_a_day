"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        node1 = l1
        node2 = l2
        while l1 or l2:
            if node1 == None and node2 == None:
                break
            elif node1 == None:
                result.append(node2)
                node2 = node2.next
            elif node2 == None:
                result.append(node1)
                node1 = node1.next

            elif node1.val <= node2.val:
                result.append(node1)
                node1 = node1.next
            else:
                result.append(node2)
                node2 = node2.next

        for element in range(len(result)):
            if result[element] == result[-1]:
                result[element].next = None
            else:
                result[element].next = result[element + 1]

        if len(result) == 0:
            return None
        else:
            return result[0]