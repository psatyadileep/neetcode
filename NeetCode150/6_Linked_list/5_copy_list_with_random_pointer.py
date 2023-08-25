"""
LC138 : https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Observations:
-> every single node has a random pointer to another node in the lsit
-> We have to look into how to create a link to the subsequent nodes

Edge cases:
-> The node might to another node which is not yet created
-> the node might point to None which is not a node

Algorithm:
-> We will use two passes
-> we will use a hash to store a maps of old and their new node copies
-> Iterate through the old list while mapping them and creating copy nodes witjout any links
-> now iterate the second time linking the next and random pointers using the hashmap
-> retrive the first head in the copy list using map[head]
-> make sure the None edge case is handled in the hasmp
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        old_to_copy = {None: None}
        while curr:
            copy = ListNode(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next


        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next



        return old_to_copy[head]





