from linked_list import LinkedList

llist = LinkedList()
print(llist)

llist.insertAtBegin(5)
llist.insertAtBegin(6)
llist.insertAtBegin(7)
print(llist)

llist.insetAtIndex(3, 1)
print(llist)

llist.insertAtEnd(2)
print(llist)

llist.updateNode(10, 0)
print(llist)

llist.remove_at_index(0)
print(llist)

llist.remove_first_node()
llist.remove_last_node()
print(llist)

print(llist.sizeOfLL())