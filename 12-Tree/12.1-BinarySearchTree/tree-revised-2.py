class BinaryNode():
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right


class BinaryTree():
	def __init__(self):
		self.node=BinaryNode()

	"""
	considering this as Binay Search Tree
	"""
	def insert(self, data):
		if self.node.data==None:
			self.node=BinaryNode(data=data)
		else:
			ptr=self.node
			while ptr.data!=None:
				if ptr.data>data:
					if ptr.left==None:
						ptr.left=BinaryNode(data=data)
						break
					else:
						ptr=ptr.left
				elif ptr.data<data:
					if ptr.right==None:
						ptr.right=BinaryNode(data=data)
						break
					else:
						ptr=ptr.right
				else:
					break

	def show(self, ptr, mode='LNR'):
		if ptr.left!=None and ptr.left.data!=None:
			self.show(ptr=ptr.left, mode=mode)
		if ptr!=None and ptr.data!=None:
			print(str(ptr.data)+"->", end='')
		if ptr.right!=None and ptr.right.data!=None:
			self.show(ptr=ptr.right, mode=mode)


	def depth(self, ptr, depth=0):
		ldepth=rdepth=depth
		if ptr!=None and ptr.data!=None:
			ldepth=rdepth=depth+1
			if ptr.left!=None and ptr.left.data!=None:
				ldepth=self.depth(ptr.left, depth+1)
			if ptr.right!=None and ptr.right.data!=None:
				rdepth=self.depth(ptr.right, depth+1)
		return ldepth if ldepth>rdepth else rdepth

	def isFullBinaryTree(self, ptr):
		if ptr!=None and ptr.data!=None:
			if (ptr.left==None or ptr.left.data==None) and (ptr.right==None or ptr.right.data==None):
				return True
			elif (ptr.left==None or ptr.left.data==None) and (ptr.right!=None and ptr.right.data!=None):
				return False
			elif (ptr.left!=None and ptr.left.data!=None) and (ptr.right==None or ptr.right.data==None):
				return False
			else:
				return self.isFullBinaryTree(ptr.left) and self.isFullBinaryTree(ptr.right)

	def search(self, ptr, ele):
		if self.node.data==None:
			return False
		else:
			if ptr.data>ele:
				if ptr.left!=None:
					return self.search(ptr=ptr.left, ele=ele)
				else:
					return False
			elif ptr.data<ele:
				if ptr.right!=None:
					return self.search(ptr=ptr.right, ele=ele)
				else:
					return False
			elif ptr.data==ele:
				return True
			else:
				return False

	def isCompleteBinaryTree(self, flag=False):
		if self.node==None or self.node.data==None:
			flag=True
		else:
			queue=[self.node,]
			while len(queue)>0:
				ptr=queue.pop(0)
				if ptr.left==None or ptr.left.data==None:
					flag=True
				else:
					if flag:
						flag=False
						break
					queue.append(ptr.left)
					flag=False
				if ptr.right==None or ptr.right.data==None:
					flag=True
				else:
					if flag:
						flag=False
						break
					queue.append(ptr.right)
					flag=False
		return flag

def main():
	tree = BinaryTree()
	lst = list(map(int, input('Enter sequence of input (SPACE SPERATED):').split()))

	for l in lst:
		tree.insert(l)

	print('Tree:', end=' ')
	tree.show(tree.node)
	print()

	print('Depth', tree.depth(tree.node))

	print('Full Binay Tree:', tree.isFullBinaryTree(tree.node))

	print('Searched Result:', tree.search(tree.node, int(input("Element to be searched:"))))

	print('Complete Binary Tree:', tree.isCompleteBinaryTree())

if __name__=='__main__':
	main()
