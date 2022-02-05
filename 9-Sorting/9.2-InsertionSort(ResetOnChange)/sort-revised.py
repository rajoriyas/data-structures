# Without Spaces
#str = list(input('Enter Statement:'))
# With Spacees
str = list(map(int, input('Enter Statement: ').split()))
i=0
while i<len(str)-1:
    if str[i]>str[i+1]:
        str[i]=str[i]+str[i+1]
        str[i+1]=str[i]-str[i+1]
        str[i]=str[i]-str[i+1]
        j=i
        while j-1>=0:
            if str[j-1]>str[j]:
                str[j]=str[j]+str[j-1]
                str[j-1]=str[j]-str[j-1]
                str[j]=str[j]-str[j-1]
                j-=1
            else:
                j=0
    i+=1
print(str)
