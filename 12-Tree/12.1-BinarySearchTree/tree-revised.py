class BinaryNode():
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right

class BinaryTree():
	def __init__(self):
		self.node = BinaryNode()

	"""
	considering this as Binay Search Tree
	"""
	def insert(self, data):
		if self.node is None or self.node.data is None:
			self.node = BinaryNode(data=data)
		else:
			ptr = self.node
			while ptr is not None and ptr.data is not None:
				if ptr.data>data:
					if ptr.left is not None and ptr.left.data is not None:
						ptr = ptr.left
					else:
						ptr.left = BinaryNode(data=data)
						break
				elif ptr.data<data:
					if ptr.right is not None and ptr.right.data is not None:
						ptr = ptr.right
					else:
						ptr.right = BinaryNode(data=data)
						break
				else:
					print('Element is already exists.', data)
					break

	def show(self, node, mode='LNR'):
		if node is not None:
			if mode == 'LNR':
				if node.left is not None and node.left.data is not None:
					self.show(node=node.left, mode='LNR')
				if node is not None and node.data is not None:
					print(node.data, end=' ')
				if node.right is not None and node.right.data is not None:
					self.show(node=node.right, mode='LNR')
			if mode == 'NLR':
				if node is not None and node.data is not None:
					print(node.data, end=' ')
				if node.left is not None and node.left.data is not None:
					self.show(node=node.left, mode='NLR')
				if node.right is not None and node.right.data is not None:
					self.show(node=node.right, mode='NLR')
			if mode == 'LRN':
				if node.left is not None and node.left.data is not None:
					self.show(node=node.left, mode='LRN')
				if node.right is not None and node.right.data is not None:
					self.show(node=node.right, mode='LRN')
				if node is not None and node.data is not None:
					print(node.data, end=' ')

	def depth(self, node, depth=0):
		if node is not None and node.data is not None:
			depth = max(self.depth(node=node.left, depth=depth+1), self.depth(node=node.right, depth=depth+1))
		return depth

	def isFullBinaryTree(self, node):
		if node is not None and node.data is not None:
			if (node.left is None or node.left.data is None) and (node.right is None or node.right.data is None):
				return True
			elif (node.left is not None and node.left.data is not None) and (node.right is not None and node.right.data is not None):
				return self.isFullBinaryTree(node=node.left) and self.isFullBinaryTree(node=node.right)
			else:
				return False

	def search(self, node, ele):
		if node.data<ele and node.right is not None and node.right.data is not None:
			return self.search(node.right, ele)
		elif node.data>ele and node.left is not None and node.left.data is not None:
			return self.search(node.left, ele)
		elif node.data==ele:
			return node
		else:
			print('Element not found!')
			return None

	def isCompleteBinaryTree(self, node, len_):
		flag=True
		queue=list()

		if node is not None and len(queue)==0:
			queue.append(node.data)
		ele = queue.pop(0)

		while ele is not None:
			ptr=self.search(node, ele)
			if ptr.left is not None and ptr.left.data is not None:
				queue.append(ptr.left.data)
			else:
				queue.append(None)

			if len(queue)>1 and queue[-2] is None and queue[-1] is not None:
				flag=False
				return flag

			if ptr.right is not None and ptr.right.data is not None:
				queue.append(ptr.right.data)
			else:
				queue.append(None)

			if len(queue)>1 and queue[-2] is None and queue[-1] is not None:
				flag=False
				return flag

			ele = queue.pop(0)
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

	print('Complete Binary Tree:', tree.isCompleteBinaryTree(tree.node, len(lst)))

if __name__=='__main__':
	main()
