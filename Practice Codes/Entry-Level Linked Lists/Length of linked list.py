# Finding the length of given linked list

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


def getCount(self, head):

    if not head:
        return 0

    curr = head
    count = 0

    while curr:
        count += 1
        curr = curr.next

    return count
