"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = next_node
        head = new_head
        return head