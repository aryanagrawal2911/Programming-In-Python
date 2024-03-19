"""
Given a Singly Linked List, delete all alternate nodes of the list.
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



def deleteAlt(self, head):

    if head.next == None:
        return

    curr = head

    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
