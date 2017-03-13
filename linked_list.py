
class  Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, self.head)
    

                               
