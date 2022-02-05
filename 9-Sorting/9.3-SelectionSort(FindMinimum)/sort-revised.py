lst = list(map(int, input('Enter expression:').split()))
for i in range(len(lst)):
	min_idx=i
	for j in range(i+1, len(lst)):
		if lst[min_idx]>lst[j]:
			min_idx=j
	lst[min_idx], lst[i] = lst[i], lst[min_idx]
print('Sorted Expression:', lst)
