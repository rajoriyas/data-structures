"""
N = int(input())
K = int(input())
lst = list((map(int, input().split())))

n=0
while n<N:
    lst[n]%=K
    n+=1
print(sum(lst))
"""
"""
dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

id = int(input())

while True:
    if id>26:
        sum = 0
        for i in str(id):
            sum+=int(i)
        id=sum
    else:
        break
print(dict[id-1])
"""
N = int(input())
lst = list((map(int, input().split())))
prime = ""
non_prime = ""
n=0
while n<N:
    i=2
    isPrime = True
    while i<lst[n] and isPrime:
        if lst[n]%i == 0:
            isPrime = False
        i+=1
    if isPrime:
        prime+=str(lst[n])+" "
    else:
        non_prime+=str(lst[n])+" "
    n+=1
print(prime+non_prime)
