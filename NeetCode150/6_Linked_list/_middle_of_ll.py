"""
LC 876 :
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow = fast = head

        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next


        return displayll(slow)


def displayll(node):
    res =[]
    while node:
        res.append(node.val)
        node = node.next

    return res








LL1 = ListNode(1, ListNode(2, ListNode(3, (ListNode(4,(ListNode(5)))))))
print(Solution().middleNode(LL1))