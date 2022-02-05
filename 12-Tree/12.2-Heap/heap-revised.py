# https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/
# https://www.geeksforgeeks.org/linked-complete-binary-tree-its-creation/
"""
Arr[i] returns its parent node.
Arr[(2 * i) + 1] returns its left child node.
Arr[(2 * i) + 2] returns its right child node.
where i is respective parent indexing
"""
class HeapNode():
	def __init__(self, data=None, left=None, right=None, type='max'):
		self.data=data
		self.left=left
		self.right=right
		self.type=type

class Heap():
	def __init__(self):
		self.node=HeapNode()
		self.queue=list()
		self.sorted=list()

	"""
	Complete Binary Tree Insertion
	"""
	def insert(self, data):
		if self.node is None or self.node.data is None:
			self.node=HeapNode(data=data)
			self.queue.append(self.node)
		else:
			ptr=self.queue[0]
			while ptr is not None and ptr.data is not None:
				print('Node:',ptr.data)
				if ptr.left is None or ptr.left.data is None:
					self.queue.append(ptr)
					ptr.left=HeapNode(data=data)
					self.queue.append(ptr.left)
					break
				elif ptr.right is None or ptr.right.data is None:
					ptr.right=HeapNode(data=data)
					self.queue.append(ptr.right)
					break
				else:
					"""
					Parent has it's two child,
					so remove it from queue
					"""
					self.queue.pop(0)
					ptr=self.queue[0]
		self.Enqueue()
		self.Heapify()
		self.show(self.node)
		print()

	def show(self, node, mode='LNR'):
		if node.left is not None and node.left.data is not None:
			self.show(node.left)
		if node is not None and node.data is not None:
			print(node.data, end=' ')
		if node.right is not None and node.right.data is not None:
			self.show(node.right)

	def Enqueue(self):
		self.queue.clear()
		self.queue.append(self.node)
		i=0
		ptr=self.queue[i]
		while ptr is not None and ptr.data is not None:
			if ptr.left is not None and ptr.left.data is not None:
				self.queue.append(ptr.left)
			if ptr.right is not None and ptr.right.data is not None:
				self.queue.append(ptr.right)
			if i+1<len(self.queue):
				i+=1
				ptr=self.queue[i]
			else:
				break

	def Heapify(self, i=0):
		while len(self.queue)>0 and i<len(self.queue):
			ptr = self.queue[i]
			if ((2*i)+1)<len(self.queue):
				left = self.queue[(2*i)+1]
				if ptr.data<left.data:
					ptr.data, left.data = left.data, ptr.data
					self.Heapify()
			if ((2*i)+2)<len(self.queue):
				right = self.queue[(2*i)+2]
				if ptr.data<right.data:
					ptr.data, right.data = right.data, ptr.data
					self.Heapify()
			i+=1

	def sort(self):
		"""
		Similiar to deletion till the end
		"""
		"""
		for this, we require deque not queue,
		so we will treat this list as deque
		"""
		self.Enqueue()
		while len(self.queue)>0:
			ptr = self.queue[0]
			self.sorted.append(ptr.data)
			last=self.queue.pop()
			ptr.data, last.data=last.data, None
			self.Heapify()

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
		    heap.sort()
		    print('Sorted:', heap.sorted)

if __name__=='__main__':
	main()
