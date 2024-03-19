"""
Given a Linked List and an integer N, find the sum of the last N nodes of the given Linked List.
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


def sumOfLastN_Nodes(self, head, m):

    reqnodes = list()
    curr = head

    while curr:

        reqnodes.append(curr.data)
        curr = curr.next
    
        if len(reqnodes) == (m + 1):
            reqnodes.pop(0)

    return sum(reqnodes)
