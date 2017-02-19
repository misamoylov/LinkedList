
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print temp.val,
            temp = temp.next

    # Time:  O(n)
    # Space: O(1)
    def copyRandomList(self, head):
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        dummy = Node(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next

    # Time:  O(n)
    # Space: O(n)
    def copyRandomListAlt(self, head):
        dummy = Node(0)
        current, prev, copies = head, dummy, {}

        while current:
            copied = Node(current.val)
            copies[current] = copied
            prev.next = copied
            prev, current = prev.next, current.next

        current = head
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            current = current.next

        return dummy.next


llist = LinkedList()
llist.add(20)
llist.add(4)
llist.add(15)
llist.add(85)

print "Given Linked List"
llist.printList()
llist.reverse()
print "\nReversed Linked List"
llist.printList()

print("\nCopy with random pointer 1")
head = Node(1)
head.next = Node(2)
head.random = head.next
result = LinkedList().copyRandomList(head)
print result.val
print result.next.val
print result.random.val

print("\nCopy with random pointer 2")
head = Node(2)
head.next = Node(3)
head.random = head.next
result = LinkedList().copyRandomListAlt(head)
print result.val
print result.next.val
print result.random.val