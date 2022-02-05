class BinaryNode():
	def __init__(self, data=None, left=None, right=None, bf=0):
		self.data=data
		self.left=left
		self.right=right
		self.bf=bf

class AVLTree():
	def __init__(self):
		self.node=BinaryNode()
	"""
	Binay Search Tree
	"""
	def insert(self, data):
		if self.node==None or self.node.data==None:
			self.node=BinaryNode(data=data)
		else:
			ptr=self.node
			while ptr!=None and ptr.data!=None:
				if ptr.data>data:
					if ptr.left!=None and ptr.left.data!=None:
						ptr=ptr.left
					else:
						ptr.left=BinaryNode(data=data)
						break
				if ptr.data<data:
					if ptr.right!=None and ptr.right.data!=None:
						ptr=ptr.right
					else:
						ptr.right=BinaryNode(data=data)
						break
		self.calculateBF(self.node)

		criticalNode=self.findCriticalNode(self.node)
		if criticalNode!=None and criticalNode.data!=None:
			self.rotate()
		print('Tree:', end=' ')
		self.show(self.node)
		print("End")

	def calculateBF(self, ptr, length=0):
		if ptr!=None and ptr.data!=None:
			left=right=length
			if ptr.left!=None and ptr.left.data!=None:
				left=self.calculateBF(ptr=ptr.left, length=length+1)
			if ptr.right!=None and ptr.right.data!=None:
				right=self.calculateBF(ptr=ptr.right, length=length+1)
			ptr.bf=left-right
			length=max(left, right)
		return length

	def show(self, ptr, mode='LNR', init="N"):
		if mode=="LRN":
			if ptr.left!=None and ptr.left.data!=None:
				self.show(ptr.left)
			if ptr.right!=None and ptr.right.data!=None:
				self.show(ptr.right)
			if ptr!=None and ptr.data!=None:
				print(str(ptr.data)+"("+str(ptr.bf)+") ->", end="")
		elif mode=="LNR":
			if ptr.left!=None and ptr.left.data!=None:
				self.show(ptr.left, init=init+"L")
			if ptr!=None and ptr.data!=None:
				print(str(ptr.data)+"("+str(ptr.bf)+")"+"("+init+") -> ", end="")
			if ptr.right!=None and ptr.right.data!=None:
				self.show(ptr.right, init=init+"R")
		if mode=="NLR":
			if ptr!=None and ptr.data!=None:
				print(str(ptr.data)+"("+str(ptr.bf)+") ->", end="")
			if ptr.left!=None and ptr.left.data!=None:
				self.show(ptr.left)
			if ptr.right!=None and ptr.right.data!=None:
				self.show(ptr.right)

	def findCriticalNode(self, ptr):
		if ptr!=None and ptr.data!=None:
			if abs(ptr.bf)>1:
				return ptr
			else:
				left=self.findCriticalNode(ptr.left)
				if left!=None and left.data!=None:
					return left
				right=self.findCriticalNode(ptr.right)
				if right!=None and right.data!=None:
					return right
		return None

	def findRotation(self, ptr, path=''):
		if ptr!=None and ptr.data!=None:
			leftPath=rightPath=path
			if ptr.left!=None and ptr.left.data!=None:
				leftPath=self.findRotation(ptr=ptr.left, path=path+"L")
			if ptr.right!=None and ptr.right.data!=None:
				rightPath=self.findRotation(ptr=ptr.right, path=path+"R")
			path=leftPath if len(leftPath)>len(rightPath) else rightPath
		return path

	def rotate(self):
		criticalNode=self.findCriticalNode(self.node)
		if criticalNode!=None and criticalNode.data!=None:
			if self.findRotation(criticalNode)[:2]=="LL":
				"""
					     z                                      y
					    / \                                   /   \
					   y   T4      Right Rotate (z)          x      z
					  / \          - - - - - - - - ->      /  \    /  \
					 x   T3                               T1  T2  T3  T4
					/ \
				  T1   T2
				"""
				criticalNode.right=BinaryNode(data=criticalNode.data, left=criticalNode.left.right, right=criticalNode.right)
				criticalNode.data=criticalNode.left.data
				criticalNode.left=criticalNode.left.left
			elif self.findRotation(criticalNode)[:2]=="LR":
				"""
				     z                               z                           x
				    / \                            /   \                        /  \
				   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
				  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
				T1   x                          y    T3                    T1  T2 T3  T4
				    / \                        / \
				  T2   T3                    T1   T2
				"""
				criticalNode.right=BinaryNode(data=criticalNode.data, left=criticalNode.left.right.right, right=criticalNode.right)
				criticalNode.data=criticalNode.left.right.data
				criticalNode.left.right=criticalNode.left.right.left
			elif self.findRotation(criticalNode)[:2]=="RR":
				"""
				  z                                y
				 /  \                            /   \
				T1   y     Left Rotate(z)       z      x
				    /  \   - - - - - - - ->    / \    / \
				   T2   x                     T1  T2 T3  T4
				       / \
				     T3  T4
				"""
				criticalNode.left=BinaryNode(data=criticalNode.data, left=criticalNode.left, right=criticalNode.right.left)
				criticalNode.data=criticalNode.right.data
				criticalNode.right=criticalNode.right.right
			elif self.findRotation(criticalNode)[:2]=="RL":
				"""
				   z                            z                            x
				  / \                          / \                          /  \
				T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
				    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
				   x   T4                      T2   y                  T1  T2  T3  T4
				  / \                              /  \
				T2   T3                           T3   T4
				"""
				criticalNode.left=BinaryNode(data=criticalNode.data, left=criticalNode.left, right=criticalNode.right.left.left)
				criticalNode.data=criticalNode.right.left.data
				criticalNode.right.left=criticalNode.right.left.right
		self.calculateBF(self.node)

def main():
	tree = AVLTree()
	lst = list(map(int, input('Enter sequence of input (SPACE SPERATED):').split()))
	for l in lst:
		tree.insert(l)

if __name__=='__main__':
	main()
