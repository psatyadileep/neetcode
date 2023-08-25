"""
LC707: Design a linked list
https://leetcode.com/problems/design-linked-list/
"""


class ListNode:
    def __init_(self, val):
        self.val = val
        self.prev = None
        self.next = None


"""
Creating two dummy nodes and adding and deleting between the dummy nodes reduces a lot of edge cases

 Left Dummy Node ->     Nodes  -> Nodes   -> Right Dummy Node
                     <-         <-         <-

"""


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1

    def addAtHead(self, val: int) -> None:
        """
        Creta a new node
        leftDummy    ->    new node   -> other element    ->          Right Dymmy
                                      <-                     <-
                       <-
        """

        node , next, prev= ListNode(val) , self.left.next , self.left
        prev.next = node , next.prev = node
        node.next = next , node.prev = prev
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.right
        prev = self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def addAtIndex(self, index: int, val: int) -> None:

        current = self.left.next
        while current and index>0 :
            current = current.next
            index-=1

        if current and index ==0 :
            node = ListNode(val)
            next = current
            prev = current.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next

        while current and index<0:
            current = current.next
            index-=1

        next = current
        prev = current.prev
        prev .next  =next
        next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)