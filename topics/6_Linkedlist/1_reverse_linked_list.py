
"""
https://leetcode.com/problems/reverse-linked-list/
Time Complexity = o(n)
Space Complexity = 0 (1)
"""
class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
#
#
# class Solution:
#
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         prev = None
#         current = head
#
#         while current:
#
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#
#
#         return prev
"""
Intution:
None-> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> Null
prev   curr 

         None <- 1 <- 2 ->    3 ->    4 ->    5 -> 6
        prev    curr    nexr

"""



class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr= head

        while curr:
            next = current.next
            curr.next = prev
            prev = curr
            curr = next


        return prev



