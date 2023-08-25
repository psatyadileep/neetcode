
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def lengthCycle(self, head)-> int:
        slow = head
        fast = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                length = 1
                slow = slow.next
                while slow!=fast:
                    slow = slow.next
                    length+=1
                return length+1

        return 0

#Test Case 2:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = None
# Expected Output: 0
print(Solution().lengthCycle(head))


# Test Case 3:
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = head2.next # Creating a cycle
# Expected Output: 4
print(Solution().lengthCycle(head2))
