# Adjacency Matrix		
class Graph():
	def __init__(self, size=0):
		self.size = size
		self.matrix = [[0 for i in range(self.size)] for j in range(self.size)] 
		self.vertics = [None]*size
	
	def insert(self, vertics):
		for i in range(self.size):
			if self.vertics[i] == vertics:
				print('Vertics exists!')
				return	
		for i in range(self.size):
			if self.vertics[i] is None:
				self.vertics[i] = vertics				
				self.show()
				return 
		print('Graph is overflow!')
	
	def hop(self, source, destination, weight):
		for i in range(self.size):
			for j in range(self.size):
				if self.vertics[i]==source and self.vertics[j]==destination:
					self.matrix[i][j] = weight
					print(i, j)
		self.show()						
	
	def show(self):
		print('Size:', self.size)
		for i in range(self.size):
			print(str(self.vertics[i])+':', self.matrix[i])
		

def main():
	graph = Graph(int(input('Size:')))
	end = False
	while not end:
		print('1:Add Vertics\n2:Add Edges\n3:Show')	
		choice = input('Choice:')
		if choice == '1':
			graph.insert(input('Vertics:'))
		elif choice == '2':
			graph.hop(input('Source:'), input('Destination:'), int(input('Weight:')))
		elif  choice == '4':
			end = True
		else:
			print('Invalid Choice')

if __name__=='__main__':
	main()
