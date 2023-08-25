class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        next_node = self.head.next

        new_node.prev = self.head
        new_node.next = next_node
        self.head.next = new_node
        next_node.prev = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        prev_node = self.tail.prev

        new_node.prev = prev_node
        new_node.next = self.tail
        prev_node.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            new_node = ListNode(val)
            prev = curr.prev
            new_node.next = curr
            new_node.prev = prev
            prev.next = new_node
            curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0 and curr != self.tail:
            prev = curr.prev
            next_node = curr.next
            prev.next = next_node
            next_node.prev = prev
