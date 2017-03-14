from linked_list import LinkedList


def removeDuplicates(l):
    s = set()
    for x in l:
        if x in s:
            l.remove(x)
        else:
            s.add(x)


def slowRemoveDuplicates(l):
    i = l.head
    while i is not None:
        j = i
        while j is not None and j.next is not None:
            if j.next.value == i.value:
                j.next = j.next.next
            j = j.next
        i = i.next

l = LinkedList()
for x in [3, 2, 4, 8, 9, 7, 3, 2, 9, 0, 5, 8,
          7, 1, 2, 0, 0, 9, 3, 5, 7, 0, 1, 9, 3, 8, 5, 6, 1, 3]:
    l.add(x)

slowRemoveDuplicates(l)

for x in l:
    print(x)
