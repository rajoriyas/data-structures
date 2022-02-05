from DynamicStackLinkedList import *

class Prefix():
	def __init__(self, exp):
		self.infix = exp[::-1]
		self.stack = Stack()
		self.prefix = list()
		self.precedence = {'^':3, '%':2, '/':2, '*':2, '-':1, '+':1}
		self.open = ['[', '{', '(']
		self.close = [']', '}', ')']
		
	def convertor(self):
		for ele in self.infix:
			if ele not in self.precedence and ele not in self.open and ele not in self.close:
				self.prefix.append(ele)
			else:
				if self.stack.top == -1:
					self.stack.push(ele)
				else:
					"""
					it's prefix so it's a reversed,
					so opening braket complete the equation,
					so if it is not a opening bracket
					"""					
					if ele not in self.open:
						"""
						if closing direct insert without validation
						"""						
						if ele in self.close:
							self.stack.push(ele)
						else:							
							temp = self.stack.pop()
							while temp not in self.close:
								if self.precedence[temp] >= self.precedence[ele]:							
									self.prefix.append(temp)
									if self.stack.top > -1:
										temp = self.stack.pop()
									else:
										break	
								else:
									self.stack.push(temp)
									break	
							"""
							if temp was a closing bracket,
							then it must be reinserted, because it must be present for it's opening
							"""					
							if temp in self.close:
								self.stack.push(temp)																
							self.stack.push(ele)
					else:
						temp = self.stack.pop()
						while temp not in self.close:
							self.prefix.append(temp)
							temp = self.stack.pop()
		while self.stack.top != -1:
			self.prefix.append(self.stack.pop())		
		print('Prefix Expression:', self.prefix[::-1])
		self.prefix = self.prefix[::-1]
		#self.stack.display()	
		
class BinaryNode():
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right	
		
class BinaryTree():
	def __init__(self, prefix):
		self.symbol = {'^':3, '%':2, '/':2, '*':2, '-':1, '+':1}
		self.prefix = prefix
		print(self.prefix)
		
	def insert(self, node):	
		if node.data == None:			
			node=BinaryNode(data=self.prefix.pop(0))
		if node.data in self.symbol:
			if len(self.prefix)>0:
				node.left=BinaryNode(data=self.prefix.pop(0))
				self.insert(node.left)				
			if len(self.prefix)>0:
				node.right=BinaryNode(data=self.prefix.pop(0))
				self.insert(node.right)	
		return node	
		
	def display(self, node):
		if node.left is not None and node.left.data is not None:
			self.display(node.left)	
		if node.data is not None:
			print(node.data, end='')
		if node.right and node.right.data is not None:
			self.display(node.right)
					
def main():
	exp = list(input('Enter Expression:'))
	prefix = Prefix(exp)	
	prefix.convertor()
	tree = BinaryTree(prefix.prefix)
	node = BinaryNode()
	node=tree.insert(node)
	tree.display(node)
	print()
	
	
if __name__ == '__main__':
	main()
