# Printing a given Linked List.


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


def displayLL(self, head):

    curr = head

    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next

    print()