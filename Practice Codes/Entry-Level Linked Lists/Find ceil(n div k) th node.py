"""
Given a linked list and an integer k, Write a function to find the (N/k)th element.
N is the number of elements in the list. We need to consider ceil value in case of decimals.
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


from math import ceil

def fractionalNodes(head, k):

    if not head:
        return -1

    co = 1
    curr = head

    while curr.next:
        co += 1
        curr = curr.next

    if k > co:
        return head.data

    reqpos = ceil(co / k)
    curr = head
    pos = 1

    while pos < reqpos:
        pos += 1
        curr = curr.next

    return curr.data
