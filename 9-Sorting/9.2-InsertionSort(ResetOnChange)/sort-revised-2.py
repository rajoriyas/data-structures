# Without Spaces
#str = list(input('Enter Statement:'))
# With Spacees
str = list(map(int, input('Enter Statement: ').split()))
i=0
while i<len(str):
    s=str[i]
    j=i-1
    while j>=0 and str[j]>s:
        str[j+1] = str[j]
        j-=1
    str[j+1]=s
    print(str)
    i+=1
print(str)
