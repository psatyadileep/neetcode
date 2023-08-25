"""
Count Elements in a Linked List (Iterative/Recursive)
"""

class ListNode:

    def __init__(self,value =0, next = None):
        self.value = 0
        self.next = 0



def countIterative(node:ListNode)-> int:

    length = 0

    while node is not None:
        node = node.next
        length+=1
    return length


def countRecursive(node: ListNode) ->int:
    if node is None:
        return 0
    return 1 + count(node.next)


