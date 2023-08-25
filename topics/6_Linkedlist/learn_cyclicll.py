
"""
8 -> 9 ->2 -> 7 -  8
"""

class listNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next



class CLL:

    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self,val):
        newNode = listNode(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode

        self.tail.next = newNode
        newNode.next = self.head
        self.tail = newNode

    def display(self):
        current = self.head

        while current is not None:
            print(current.val,end="->")
            current = current.next
            if current == self.head:
                print("end")
                return




cll = CLL()

cll.insert(23)
cll.insert(3)
cll.insert(19)
cll.insert(75)
cll.display()