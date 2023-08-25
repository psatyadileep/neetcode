"""
there are two ways of insertion
-> void return type and makes change sin LL
-> node return type that returns the List Node
"""

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class LL():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        self.tail = None

    def insert_recurion(self,val , indx, node):
        if index == 0 :
            newNode = ListNode(val)
            return newNode
