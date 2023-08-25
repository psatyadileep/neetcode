"""
LC21: Merge Two sorted Lsist

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val> list2.val:
                tail.next = list1

            else:
                tail.next  = list2


            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next




