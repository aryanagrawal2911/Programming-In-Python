# Given a linked list consisting of L nodes and given a number N.
# The task is to find the Nth node from the end of the linked list.


'''
Node Class used
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
     

"""
Linked List used
"""
class Linked_List:
    def __init__(self):
        self.head = None


def getNthFromLast(head,n):

# Using two-pointer approach
    fast = slow = head

    for _ in range(n):
        if fast is None:
            return -1
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.data