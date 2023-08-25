"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

1- > 2  - > 3  - > 4 - > 5 - > 6
slow
fast

1   ->  2   ->  3   ->  4   ->  5   ->  6
        slow
                fast

1   ->  2   ->  3   ->  4   ->  5   ->  6-> None
                       slow
                                          fast
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fasr = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
