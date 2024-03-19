"""
Given a singly linked list of N nodes.
The task is to find the middle of the linked list.
If there are two middle nodes(in case, when N is even),
print the second middle element.
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



def findMid(self, head):

    if not head:
        return -1

    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.data
