choice = input('1:Integer\n2:Character\nEnter Choice:')
seq = list(input('Enter Statement: ').split(' '))
if choice=='1':
    seq = [int(s) for s in seq]

count=0
def compare(seq):
	lb=0
	ub=len(seq)-1
	mid=(lb+ub)//2
	print(seq)
	if ub>lb: 		
		pre=list()
		post=list()
		for i in range(len(seq)):
			if i<=mid:
				pre.append(seq[i])
			else:
				post.append(seq[i])
		pre=compare(pre)
		post=compare(post)
		sorted_=sort(pre, post)
		print(sorted_)
		return sorted_
	return seq
	
def sort(pre, post):
	sorted_=list()
	i=j=0
	while i<len(pre) and j<len(post):
		if pre[i]<post[j]:
			sorted_.append(pre[i])
			i+=1
		else:
			sorted_.append(post[j])
			j+=1
	while i<len(pre):
		sorted_.append(pre[i])
		i+=1
	while j<len(post):
		sorted_.append(post[j])
		j+=1
	return sorted_
	
print(compare(seq))
