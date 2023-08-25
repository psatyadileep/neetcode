"""
LC 141: Linked List Cycle

fast and slwo pointer emthod
used for two things: Cycle detection and landing a node'

anytime a question with cycle comes we need to used the fast and slow pointer method

if the fast and slow pointers are meeting a point that means a cycle is present else
the fast point should go to end
# """
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True


        return False




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next # Creating a cycle


print(Solution().hasCycle(head))
