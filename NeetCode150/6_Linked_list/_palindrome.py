"""
LC234: https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.

 Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false


""'
Algo : using 2 passes and a sentinel node
->  iterate through the head and save the nodes in a  list
-> now reverse all the nodes and save the list
-> check if the first list is equal to the second list
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:

        res1 = displayll(head)

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        res2 = displayll(prev)

        return res1 == res2

def displayll(node):
    res =[]
    while node:
        res.append(node.val)
        node = node.next

    return res





LL1 = ListNode(1,ListNode(2, ListNode(2,(ListNode(1)))))
print(Solution().isPalindrome(LL1))
