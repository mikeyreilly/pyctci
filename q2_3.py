from linked_list import LinkedList


def removeNodeMiddle(lst, node):
    # our LinkedList is only singly linked
    # so we have to find the previous node
    # The slow way
    n = lst.head
    while n is not None:
        if n.next == node:
            n.next = n.next.next
            return
        n = n.next


l = LinkedList()
for x in [3, 2, 4, 8, 9, 7, 3, 2, 9, 0, 5, 8]:
    l.add(x)

print("before")
for x in l:
    print(x)


n = l.head
for i in range(5):
    n = n.next

print("will remove ", n.value)

removeNodeMiddle(l, n)

print("after")
for x in l:
    print(x)
