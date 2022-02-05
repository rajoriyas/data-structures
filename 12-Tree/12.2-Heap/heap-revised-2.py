# https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/
# https://www.geeksforgeeks.org/linked-complete-binary-tree-its-creation/
"""
Arr[i] returns its parent node.
Arr[(2 * i) + 1] returns its left child node.
Arr[(2 * i) + 2] returns its right child node.
where i is respective parent indexing
"""
from copy import deepcopy

class HeapNode():
	def __init__(self, data=None, left=None, right=None, type='min'):
		self.data=data
		self.left=left
		self.right=right
		self.type=type

class Heap():
	def __init__(self):
		self.node=HeapNode()
	"""
	Complete Tree 
	"""
	def insert(self, data):
		if self.node==None or self.node.data==None:
			self.node=HeapNode(data=data)
		else:
			queue=[self.node,]
			ptr=queue.pop(0)
			while ptr!=None and ptr.data!=None:
				if ptr.left!=None and ptr.left.data!=None:
					queue.append(ptr.left)
				else:
					ptr.left=HeapNode(data=data)
					break
				if ptr.right!=None and ptr.right.data!=None:
					queue.append(ptr.right)
				else:
					ptr.right=HeapNode(data=data)
					break
				ptr=queue.pop(0)
		self.Heapify()
		self.show(ptr=self.node)
		print("End")

	def show(self, ptr, mode='NLR'):
		if ptr!=None and ptr.data!=None:
			print(str(ptr.data)+"->", end="")
		if ptr.left!=None and ptr.left.data!=None:
			self.show(ptr=ptr.left)
		if ptr.right!=None and ptr.right.data!=None:
			self.show(ptr=ptr.right)

	def Enqueue(self):
		pass

	def Heapify(self, i=0):
		if i>=0:
			lst=[self.node,]
			while len(lst)>i and lst[i]!=None and lst[i].data!=None:
				if lst[i].left!=None and lst[i].left.data!=None:
					lst.append(lst[i].left)
				if lst[i].right!=None and lst[i].right.data!=None:
					lst.append(lst[i].right)
				if (2*i)+1<len(lst) and lst[i].data>lst[(2*i)+1].data:
					lst[i].data+=lst[(2*i)+1].data
					lst[(2*i)+1].data=lst[i].data-lst[(2*i)+1].data
					lst[i].data=lst[i].data-lst[(2*i)+1].data
					self.Heapify(i=int((i-1)/2))
				if (2*i)+2<len(lst) and lst[i].data>lst[(2*i)+2].data:
					lst[i].data+=lst[(2*i)+2].data
					lst[(2*i)+2].data=lst[i].data-lst[(2*i)+2].data
					lst[i].data=lst[i].data-lst[(2*i)+2].data
					self.Heapify(i=int((i-2)/2))
				i+=1

	def sort(self):
		lst=[self.node,]
		i=0
		while len(lst)>i and lst[i]!=None and lst[i].data!=None:
			if lst[i].left!=None and lst[i].left.data!=None:
				lst.append(lst[i].left)
			if lst[i].right!=None and lst[i].right.data!=None:
				lst.append(lst[i].right)
			i+=1

		sortedLst=[]
		while len(lst)>0 and lst[0]!=None and lst[0].data!=None:
			ptr=lst[0]
			last=lst.pop()

			sortedLst.append(ptr.data)

			ptr.data, last.data=last.data, None
			self.Heapify()

		return sortedLst

def main():
	node = HeapNode()
	heap = Heap()
	process=True
	while process:
		print('1:Insert\n2:Sort\n3:Exit')
		choice=input('Choice:')
		if choice=='3':
		    process=False
		    break
		elif choice=='1':
		    heap.insert(int(input('Element:')))
		elif choice=='2':
		    print('Sorted:', heap.sort())

if __name__=='__main__':
	main()
