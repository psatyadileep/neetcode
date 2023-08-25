"""
LC141: Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
 Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


"""
"""
Time Dompelxity = O(n)
Space COmplexity = o(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:

        slow , fast  = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

print(Solution().hasCycle(a))