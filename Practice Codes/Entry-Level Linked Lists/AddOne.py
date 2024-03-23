'''
You're given a positive integer represented in the form of a singly linked-list of digits.
The length of the number is 'n'.
Add 1 to the number, i.e., increment the given number by one.
The digits are stored such that the most significant digit is at the head of the linked list
and the least significant digit is at the tail of the linked list.
'''


# Node class used :
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



# The method returns the head of the linked list
def addOne(head: Node) -> Node:
    curr = head
    arr = []

    while curr.next:
        arr.append(curr.data)
        curr = curr.next

    arr.append(curr.data)

    if 0 <= curr.data <= 8:
        curr.data += 1
        return head

    else:
        n = int(''.join(str(ch) for ch in arr)) + 1
        arr.clear()
        co = 0

        for dig in str(n):
            arr.append(int(dig))
            co += 1

        i = 0
        nhead = Node(arr[i])
        curr = nhead

        while i < co:
            i += 1

            if i == co:
                break

            curr.next = Node(arr[i])
            curr = curr.next

        return nhead




'''

Sample I/O to test the code Execution

n = int(input())
data = input().strip().split()

i = 0
head = Node(data[i])
curr = head

while i < n:
    i += 1

    if i == n:
        break

    curr.next = Node(data[i])
    curr = curr.next

new_head = addOne(head)
curr = new_head

while curr:
    print(curr.data, end = " ")
    curr = curr.next
print()
'''