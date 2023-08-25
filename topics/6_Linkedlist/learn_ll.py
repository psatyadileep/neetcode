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


    def insert_at_beginning(self,val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        if not self.tail:
            self.tail = self.head

        self.size+=1


    def insert_at_end(self,val):
        newNode = ListNode(val)

        if not self.tail :
            self.insert_at_beginning(val)
            return
        self.tail.next = newNode
        self.tail = newNode
        # if self.head is None:
        #     self.head = newNode
        # else:
        #     current = self.head
        #     while current.next is not None:
        #         current = current.next
        #
        #     current.next = newNode

        self.size+=1

    def insert_at_index(self,val,index):
        newNode = ListNode(val)
        if index ==0:
            self.insert_at_beginning(val)
            return
        if index == self.size:
            self.insert_at_end(val)
            return
        if index>self.size:
            self.tail.next = newNode
            self.tail  = newNode
            return
        current = self.head
        count = 1
        while count<index:
            current = current.next
            count += 1
        temp = current.next
        current.next = newNode
        newNode.next = temp
        self.size += 1

    def delete_first(self):
        value = self.head.val
        self.head  = self.head.next

        if self.head is None:
            self.tail = None
        self.size-=1
        return value

    def delete_last(self):
        if self.size<=1:
            return self.delete_first()

        ll_size = self.size
        current = self.head
        for i in range(0,self.size-2):
            print(current.val)
            current = current.next
        value = current.next.val
        current.next = None
        self.tail = current
        return value

    def delete(self,index):
        if index ==0 :
            return self.delete_first()
        if index == self.size-1:
            return self.delete_last()

        prev = self.get_index(index-1)
        value = prev.next.val
        prev.next = prev.next.next

        return value


    def get_index(self,index):
        current = self.head
        ll_size = index
        for i in range(0,index):
            current = current.next

        return current

    def find_value(self,val):
        current = self.head

        while current:
            if current.val == val:
                return current

            current = current.next

        return None














    def display(self):
        current = self.head
        while current:
            print(current.val,end="->")
            current = current.next
        print("End")

#
#
#
# class ListNode:
#     def __init__(self,info,next = None):
#         self.info = info
#         self.next = next
#
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def insert_at_beginning(self, info):
#         newNode = ListNode(info)
#         if self.head is None:
#             self.head = newNode
#         else:
#             newNode.next = self.head
#             self.head = newNode
#
#         self.size+=1
#
#
#
#     def display(self):
#
#         current = self.head
#         while current is not None:
#             print(current.info)
#             current = current.next
#
#
#

ll  = LL()
ll.insert_at_beginning(1)
ll.insert_at_beginning(8)
ll.insert_at_beginning(6)
ll.insert_at_beginning(2)
ll.insert_at_end(98)
ll.insert_at_end(100)
ll.insert_at_index(7,3)
print("Printing elements")
ll.display()
# ll.delete_first()
# ll.display()
# print(ll.get_index(1))

# ll.delete_last()
print(ll.delete(3))
ll.display()




