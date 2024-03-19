"""
Given a singly linked list and a number k,
you are required to complete the function modularNode() which returns the modular node of the linked list.
A modular node is the last node of the linked list whose Index is divisible by the number k, i.e. i%k==0.
Note: If no such node is available, return -1. We are following 1 indexing.
"""


"""
Node class used
"""
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
Linked List used
"""
class Linked_List:
    def __init__(self):
        self.head = None



def getLength(head):

    count = 0

    while head:
        count += 1
        head = head.next

    return count

def modularNode(head, k):

    l = getLength(head)

    if l == 0 or k > l or k == 0:
        return -1

    node_position = l - (l % k)

    curr = head
    position = 1

    while position != node_position:

        position += 1
        curr = curr.next
    
    return curr.data


