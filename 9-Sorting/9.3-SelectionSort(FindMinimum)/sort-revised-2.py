lst=list(map(int, input('Enter expression: ').split()))
i=0
while i<len(lst):
	min_idx=i
	j=i+1
	while j<len(lst):
		if lst[j]<lst[min_idx]:
			min_idx+=j
			j=min_idx-j
			min_idx=min_idx-j
		j+=1
	print(lst[min_idx], lst[i])
	if min_idx!=i:
		lst[min_idx]+=lst[i]
		lst[i]=lst[min_idx]-lst[i]
		lst[min_idx]=lst[min_idx]-lst[i]
	print(lst)
	i+=1
print(lst)
