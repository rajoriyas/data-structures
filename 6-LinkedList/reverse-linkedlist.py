from linkedlist import *
llist=LinkedList()
seq = list(map(str, input('Linked List:').split()))
for ele in seq:
	llist.append(ele)
	
llist.show()	
reverse=LinkedList()
def reversing(ptr):
	if ptr is not None and ptr.info is not None: 
		if ptr.next is not None and ptr.next.info is not None:
			reversing(ptr.next)
		reverse.append(ptr.info)
reversing(llist.node)
reverse.show()
