"""
Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        equal_or_grater = []
        smaller = []

        curr_node = head

        if curr_node == None:
            return None

        while curr_node:
            if curr_node.val < x:
                smaller.append(curr_node)
            else:
                equal_or_grater.append(curr_node)

            curr_node = curr_node.next

        full_list = smaller + equal_or_grater
        for i in range(len(full_list) - 1):
            full_list[i].next = full_list[i + 1]
        full_list[-1].next = None

        return full_list[0]

