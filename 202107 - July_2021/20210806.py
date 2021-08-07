"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []
        current_node = head
        while current_node != None:
            val_list.append(current_node.val)
            current_node = current_node.next

        return val_list[::1] == val_list[::-1]


