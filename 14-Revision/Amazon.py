def idealDays(days, k):
    n = len(days)
    result = []
    leftIdeal = [0 for _ in range(n)]
    rightIdeal = [0 for _ in range(n)]
    for i in range(1, n):
        if days[i] <= days[i-1]:
            leftIdeal[i] = leftIdeal[i-1] + 1
    for i in reversed(range(n-1)):
        if days[i] <= days[i+1]:
            rightIdeal[i] = rightIdeal[i+1] + 1
    for i in range(n):
        if leftIdeal[i] >= k and rightIdeal[i] >= k:
            result.append(i+1)
    print(leftIdeal, rightIdeal)
    return result
print(idealDays([3,2,2,4,3,4], 1))
"""
popularity = list(map(int, input("Orders:").split()))
k = int(input("Output Length:"))

order=[item for item in popularity]
for i in range(len(popularity)):
    sum=popularity[i]
    for j in range(len(popularity)):
        if i!=j:
            sum+=popularity[j]
            notExists=True
            for x in range(len(order)):
                if order[x]==sum:
                    notExists=False
            if notExists:
                order.insert(x, sum)
order.sort(reverse=True)
print(order[:k], order)
"""
"""
length = int(input('Length:'))
i = 0
order = []
while i<length:
    order.append(input())
    i+=1

nonPrime = []
prime = []
for item in order:
    if not item.split()[1].isalpha():
        nonPrime.append(item)
    else:
        prime.append(item)

i=0
while i<len(prime):
    j=i+1
    while j<len(prime):
        if prime[i].split(" ", 1)[1]>prime[j].split(" ", 1)[1]:
            prime[i], prime[j] = prime[j], prime[i]
        elif prime[i].split(" ", 1)[1]==prime[j].split(" ", 1)[1]:
            if prime[i].split(" ", 1)[0]>prime[j].split(" ", 1)[0]:
                prime[i], prime[j] = prime[j], prime[i]
        j+=1
    i+=1

print(prime+nonPrime)
"""
"""
lst = list(map(int, input().split()))
k = int(input())

out = []
i = k
while i<len(lst)-k:
    j = i-k
    check = True
    while j<len(lst):
        if lst[i]>lst[j]:
            check = False
            break
        j+=1
    if check:
        out.append(i+1)
    i+=1
print(out)
"""

# Spiral Form
"""
size = int(input('Size:'))
i = 0
matrix = []
while i<size:
    matrix.append(list(map(int, input().split())))
    i+=1
print(matrix)

left = 0
right = size-1
top = 0
bottom = size-1

out = []
while left<=right and top<=bottom:
    h = left
    while h<=right:
        out.append(matrix[top][h])
        h += 1

    top += 1
    v = top
    while v<=bottom:
        out.append(matrix[v][right])
        v += 1

    right -= 1
    h = right
    while h>=left:
        out.append(matrix[bottom][h])
        h -= 1

    bottom -= 1
    v = bottom
    while v>=top:
        out.append(matrix[v][left])
        v -= 1

    left += 1
print(out)
"""

# Bellman Ford Algo

"""
import math
def relaxation(path, i, j, u, v, cost=1):
    if path[i][j]+cost<path[i+u][j+v]:
        path[i+u][j+v] = path[i][j]+cost
    return path

def update_edge(i, j, path):
    if i-1>=0:
        path = relaxation(path, i, j, -1, 0)
    if i+1<size:
        path = relaxation(path, i, j, 1, 0)
    if j-1>=0:
        path = relaxation(path, i, j, 0, -1)
    if j+1<size:
        path = relaxation(path, i, j, 0, 1)
    return path

size = int(input('Size:'))
i = 0
matrix = []
while i<size:
    matrix.append(list(map(int, input().split())))
    i+=1
print(matrix)

path = [[ math.inf for y in range(size) ] for x in range(size) ]
path[0][0] = 0
print(path)

vertics = []

for i in range(size):
    for j in range(size):
        if matrix[i][j] != 0:
            vertics.append([i, j])
for _ in range(size**2 - 1):
    for coor in vertics:
        path = update_edge(coor[0], coor[1], path)
print(path)
"""

# Dijkstra’s Algo
"""

import math

size = int(input('Size:'))
i = 0
matrix = []
while i<size:
    matrix.append(list(map(int, input().split())))
    i+=1
#print(matrix)

path = [[ math.inf for y in range(size) ] for x in range(size) ]
path[0][0] = 0

def minimum(visited, matrix, path):
    x, y, val = -1, -1, math.inf
    i=0
    while i<size:
        j=0
        while j<size:
            if (i, j) not in visited and matrix[i][j]!=0 and path[i][j]<val:
                x, y, val = i, j, path[i][j]
            j+=1
        i+=1
    return x, y

visited = []
i, j = 0, 0
while i>=0 and i<size and j>=0 and j<size:
    if (i, j) not in visited and matrix[i][j]!=0:
        if matrix[i][j]==1:
            if j+1<size and path[i][j+1]>path[i][j]+1:
                path[i][j+1]=path[i][j]+1
            if j-1>=0 and path[i][j-1]>path[i][j]+1:
                path[i][j-1]=path[i][j]+1
            if i+1<size and path[i+1][j]>path[i][j]+1:
                path[i+1][j]=path[i][j]+1
            if i-1>=0 and path[i-1][j]>path[i][j]+1:
                path[i-1][j]=path[i][j]+1
        visited.append((i, j))
    i, j = minimum(visited, matrix, path)
    print(i, j, path, visited)
"""

"""
exp = 'abcbdbdsdfng'
sub = ""
i=0
while i<len(exp):
    check = True
    j=i
    while j<len(exp):
        if i!=j:
            if exp[i]==exp[j]:
                check = False

        j+=1
    if check:
        sub+=exp[i]
    else:
        sub=""
    i+=1
print(len(sub))
"""

# Using Looping
"""

n = 2
A = [1, 5]
k = 1

def get_list(A, X):
    i=0
    while i<n:
        if X[i]<=min(pow(2, k)-1, A[i]):
                X[i] = X[i] + 1
                A[i] = A[i] - X[i]
                return A, X
        i+=1

def minimumsum(n, k, A):
    X = [0]*n
    Z = None
    i = 0
    while i<n:
        if i==0:
            Z = A[i] | A[i+1]
            i+=2
        else:
            Z = Z | A[i]
            i+=1


    while Z&(pow(2, k)-1)!=0:
        A, X = get_list(A, X)

        i = 0
        while i<n:
            if i==0:
                Z = A[i] | A[i+1]
                i+=2
            else:
                Z = Z | A[i]
                i+=1
    return sum(X)

out = minimumsum(n, k, A)
print(out)
"""
