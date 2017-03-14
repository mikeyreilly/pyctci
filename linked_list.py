class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n


class LinkedListIterator:
    def __init__(self, l):
        self.current = l.head

    def __next__(self):
        if self.current is None:
            raise StopIteration

        v = self.current.value
        self.current = self.current.next
        return v


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self)

    def add(self, value):
        self.head = Node(value, self.head)

    def remove(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return

        while(current is not None):
            v = current.next.value
            if v == value:
                current.next = current.next.next
                return
            current = current.next
