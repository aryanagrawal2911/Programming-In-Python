"""
You have a linked list and you have to implement the functionalities 
push and pop of stack using this given linked list.
complete the functions push() and pop() to implement a stack.
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


class MyStack:

    def __init__(self):
        self.head = None


    #Function to push an integer into the stack.
    def push(self, data):

        newn = node(data)
        newn.next = self.head
        self.head = newn



    #Function to remove an item from top of the stack.
    def pop(self):

        if not self.head:
            return -1

        else:
            ans = self.head.data
            self.head = self.head.next
            return ans