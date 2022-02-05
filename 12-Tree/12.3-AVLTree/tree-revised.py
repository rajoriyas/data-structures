class BinaryNode():
	def __init__(self, data=None, left=None, right=None, bf=0):
		self.data=data
		self.left=left
		self.right=right
		self.bf=bf

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
		self.calculateBF(self.node)
		self.rotate()
		self.calculateBF(self.node)

	def calculateBF(self, ptr, length=0):
		if ptr is not None and ptr.data is not None:
			if ptr.left is None or ptr.left.data is None:
				left=length
			elif ptr.left is not None or ptr.left.data is not None:
				left=self.calculateBF(ptr.left, length+1)

			if ptr.right is None or ptr.right.data is None:
				right=length
			elif ptr.right is not None or ptr.right.data is not None:
				right=self.calculateBF(ptr.right, length+1)

			ptr.bf=left-right
			return max(left, right)
		return 0

	def show(self, node, mode='LNR'):
		if node is not None:
			if mode == 'LNR':
				if node.left is not None and node.left.data is not None:
					self.show(node=node.left, mode='LNR')
				if node is not None and node.data is not None:
					print(node.data, 'bf:'+str(node.bf)+',', end=' ')
				if node.right is not None and node.right.data is not None:
					self.show(node=node.right, mode='LNR')

	def findCriticalNode(self, ptr):
		if abs(ptr.bf)>1:
			return ptr.bf, ptr
		else:
			if ptr.left is not None and ptr.left.data is not None:
				left, lloc=self.findCriticalNode(ptr.left)
				if abs(left)>1:
					return left, lloc
			if ptr.right is not None and ptr.right.data is not None:
				right, rloc=self.findCriticalNode(ptr.right)
				if abs(right)>1:
					return right, rloc
		return 0, BinaryNode()

	def findRotation(self, loc, length=0, path=''):
		if loc is not None and loc.data is not None:
			if loc.left is None or loc.left.data is None:
				left=length
				l_path=path+''
			else:
				left, l_path=self.findRotation(loc.left, length+1, path=path+'L')

			if loc.right is None or loc.right.data is None:
				right=length
				r_path=path+''
			else:
				right, r_path=self.findRotation(loc.right, length+1, path=path+'R')

			if right>left:
				return right, r_path
			else:
				return left, l_path
		return length, path

	def rotate(self):
		bf, loc=self.findCriticalNode(self.node)
		_, path=self.findRotation(loc)
		if path[:2]=='LL':
			loc.data, loc.left, loc.right = loc.left.data, loc.left.left, BinaryNode(data=loc.data, left=loc.left.right, right=loc.right)

		if path[:2]=='RR':
			loc.data, loc.right, loc.left = loc.right.data, loc.right.right, BinaryNode(data=loc.data, left=loc.left, right=loc.right.left)

		if path[:2]=='RL':
			loc.data, loc.left, loc.right.left = loc.right.left.data, BinaryNode(data=loc.data, left=loc.left, right=loc.right.left.left), loc.right.left.right

		if path[:2]=='LR':
			loc.data, loc.right, loc.left.right = loc.left.right.data, BinaryNode(data=loc.data, left=loc.left.right.right, right=loc.right), loc.left.right.left
		_, bf=self.findCriticalNode(self.node)

def main():
	tree = BinaryTree()
	lst = list(map(int, input('Enter sequence of input (SPACE SPERATED):').split()))
	for l in lst:
		tree.insert(l)
	print('Tree:', end=' ')
	tree.show(tree.node)
	print()

if __name__=='__main__':
	main()
