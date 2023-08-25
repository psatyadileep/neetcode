
"""
https://leetcode.com/problems/reverse-linked-list/
Time Complexity = o(n)
Space Complexity = 0 (1)


Observations:

1-> 2 -> 3 -> 4  -> 5

-> we have nodes that are connected
-> we wanna take these linke and reverse them
->  hence the last node becomes the head



Algorithm:
-> we can use a two pointer technique with sentinel node
-> use the current node to point to the previos
-> move the temporary node and current node


   1-> 2 -> 3 -> 4  -> 5

-> prev   1-> 2 -> 3 -> 4  -> 5
        curr
-> -> None <-1       2 -> 3 -> 4  -> 5
             prev    curr
->next = curr.next , curr.next = prev
->prev = curr ,    curr = next
"""
class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current:

            next = current.next
            current.next = prev
            prev = current
            current = next


        return prev


