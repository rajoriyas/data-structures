from DynamicStackLinkedList import *

class TOH():
	def transfer(self, num, A, B, C):
		if num == 1:
			C.push(A.pop())
			return 
		"""
		step 1st
		"""
		self.transfer(num-1, A, C, B)
		"""
		step 2nd
		"""
		C.push(A.pop())
		"""
		step 3rd
		"""
		self.transfer(num-1, B, A, C)
		
def main():
	num = int(input('Enter number of disks:'))
	A = Stack()
	B = Stack()
	C = Stack()
	
	for i in range(1, num+1):
		A.push(i)	
	A.display()
	
	toh = TOH()
	toh.transfer(num, A=A, B=B, C=C)
	print('Playing')	
	C.display()
	
if __name__=='__main__':
	main()
