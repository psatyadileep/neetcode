"""
LC 83: Remove duplicates from sorted list

1  -> 1 -> 1 -> 2 -> 4 - >

1-> 2 -> 4
"""
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None 
        current = head

        while current.next is not None:
            if (current.next is not None) and (current.val == current.next.val):
                current.next = current.next.next
            else:
                current = current.next


        return head




