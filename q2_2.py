from linked_list import LinkedList


def removeKthLast(lst, k):
    '''Remove element len-k form LinkedList lst, where len is the length
of lst. E.g. l=[1, 2 , 3, 4, 5]; removeKthLast(l, 2); l==[1, 2, 3, 5] '''
    prev = None
    curr = lst.head
    ahead = curr
    for i in range(k):
        # leave the list alone if there are fewer than k elements
        if ahead is None:
            return
        ahead = ahead.next

    while ahead is not None:
        prev = curr
        curr = curr.next
        ahead = ahead.next

    if prev is None:
        # lst is k elements long
        lst.head = lst.head.next
        return

    prev.next = curr.next

l = LinkedList()
for x in [1, 2, 3, 4, 5]:
    l.add(x)

print("before")
for x in l:
    print(x)

removeKthLast(l, 0)

print("after")
for x in l:
    print(x)
