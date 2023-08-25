"""

 cuu     cur       curr
 8 ->    3   ->     2   ->  5
   <-        <-         <-
"""
"""
 8 ->    3   ->     2   ->  5
                 9 

1.print 8 , move to 3 
  tail = 8

print 3 move to 2 
print 2 move to 5
print 5 move to null
"""

class listNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev =  prev



class DLL:
    def __init__(self):

       self.head = None
       self.tail = None
       self.size = 0



    def insert_at_beginning(self,val):

        newNode = listNode(val)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode





    def display(self):
        curr = self.head
        last = None

        while curr:
            print(curr.val,end="->")
            last = curr
            curr = curr.next
        print("end")

        while last:
            print(last.val,end= "->")
            last = last.prev
        print("end")

        print("end")


    def insert_at_end(self,val):
        newNode = listNode(val)

        curr = self.head

        if not self.head:
            self.head = newNode
            return

        while curr.next:
            curr = curr.next

        curr.next = newNode
        newNode.prev = curr


    def insert_at_index(self,val,index):
        newNode = listNode(val)
        curr = self.head


    def insert_after(self,after,value):
        newNode = listNode(value)
        if not self.head:
            self.head = newNode
            return


        curr  = self.head
        while curr.val!= after :
            curr = curr.next

        if curr.next:
            next = curr.next
        else:
            next = None
        curr.next = newNode
        newNode.prev = curr
        newNode.next = next
        if next is not None:
            next.prev = newNode










dll = DLL()
dll.insert_at_beginning(1)
dll.insert_at_beginning(8)
dll.insert_at_beginning(6)
dll.insert_at_beginning(2)
dll.insert_at_end(9)
dll.display()
dll.insert_after(6,78)
dll.display()
dll.insert_after(9,100)
dll.display()




