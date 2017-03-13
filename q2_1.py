from linked_list import LinkedList

l = LinkedList()

data = [1, 2, 3, 4, 2, 5, 3, 6]

for x in data:
    l.add(x)


current = l.head
while(current != None):
    print(current.value)
    current = current.next

