"""
Input -
    12
    0 4 2 1 2 9 4 8 -1 4 -1 -1
    9 0 3 6 2 6 2 3 6 -1 -1 3
    7 1 0 10 8 9 1 3 -1 7 -1 10
    5 1 9 0 3 -1 1 10 7 1 -1 7
    -1 5 1 4 0 2 10 4 10 6 4 5
    7 8 3 7 5 0 5 1 3 5 7 2
    6 -1 6 1 10 7 0 10 -1 -1 7 7
    -1 3 2 7 4 -1 4 0 10 5 6 10
    10 6 1 10 4 4 7 10 0 4 7 4
    1 1 6 8 8 9 2 10 6 0 -1 3
    5 9 3 -1 4 3 -1 -1 -1 3 0 1
    2 2 8 6 2 4 4 3 -1 3 4 0
"""

#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		nodes=len(matrix)
		for node in range(nodes):
		    for i in range(len(matrix)):
		        for j in range(len(matrix[i])):
		            if i!=j and i!=node and j!=node:
		                if matrix[i][node]!=-1 and matrix[node][j]!=-1:
    		                if matrix[i][j]>matrix[i][node]+matrix[node][j] or matrix[i][j]==-1:
    		                    matrix[i][j]=matrix[i][node]+matrix[node][j]
		return matrix

#{
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends
