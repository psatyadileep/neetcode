"""
lc 21: Mege two soerted Lists

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


 1-> 2 -> 4
1-> 3 -> 4

1 - > 1 -> 2->  3 -> 4 - >

sentinel = None

if current2.val > current1.val
sentinel .next  = curren1

else:
    sentinel.enext = current 2

sentinel = sentinel .next

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0)
        tail = sentinel

        while list1 and list2:
            if list1.val> list2.val:
                tail.next = list2
            else:
                tail.next = list1

        sentinel = sentinel.next

        if list1:
            tail.next = list1
        if list2:
            tail.next= list2


        return sentinel.next



LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))


