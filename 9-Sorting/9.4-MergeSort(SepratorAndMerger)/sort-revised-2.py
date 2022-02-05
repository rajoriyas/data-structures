seq = list(map(int, input('Enter Statement: ').split(' ')))

def mergeSort(seq):
    if len(seq)==1:
        return seq
    mid = len(seq)//2
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])

    i=0
    j=0
    k=0
    out = [ None for _ in range(len(left)+len(right)) ]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            out[k]=left[i]
            i+=1
        else:
            out[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        out[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        out[k]=right[j]
        j+=1
        k+=1
    return out
print(mergeSort(seq))
