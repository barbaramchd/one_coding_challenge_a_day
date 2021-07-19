"""
  Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        result = []
        k_list = []
        current_node = head
        while current_node != None:
            k_list.append(current_node)
            if len(k_list) == k:
                k_list_reverse = k_list[::-1]
                result += k_list_reverse
                k_list = []
            current_node = current_node.next

        result += k_list

        for node in range(len(result) - 1):
            result[node].next = result[node + 1]
        result[-1].next = None
        return result[0]