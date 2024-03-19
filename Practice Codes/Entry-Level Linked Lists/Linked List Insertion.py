# Insertion in a linkedlist at any position

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


# Function to get length of linkedlist
def getLength(head):
    if not head:
        return 0

    count = 0

    while head:
        count += 1
        head = head.next

    return count


# Function to insert a Node at the start of the linked list.
def insertAtBegining(head, x):

    newn = node(x)
    newn.next = head


# Function to insert a Node at the end of the linked list.
def insertAtEnd(head, x):

    newn = node(x)

    if not head:
        newn.next = head
        return

    curr = head

    while curr.next:
        curr = curr.next

    curr.next = newn


# Function to insert a Node at the exact middle of the linked list.
def insertInMid(head,x):

    newn = node(x)

    slow = head
    fast = head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    newn.next = slow.next
    slow.next = newn


# Function to insert a Node at the given 0-based index position of the linked list.
def insertAtindex(head, index, x):

    if index == 0:
        insertAtBegining(head, x)
        return

    n = getLength(head)

    if index == (n // 2):
        insertInMid(head)
        return

    elif index == (n - 1):
        insertAtEnd(head, x)
        return

    newn = node(x)
    position = 0
    curr = head

    while curr:

        if position == index - 1:
            newn.next = curr.next
            curr.next = newn
            return

        positio += 1
        curr = curr.next

    else:
        raise IndexError("Index Out of range!!!")

