stmt = list(map(int, input('Statement:').split()))
ele = int(input('Element:'))

def mergeSort(seq):
    if len(seq)>1:
        mid=len(seq)//2

        """
        left=mergeSort(seq[:mid])
        right=mergeSort(seq[mid:])
        """

        left=[ None for _ in range(0, mid)]
        right=[ None for _ in range(mid, len(seq)) ]
        i=0
        j=0
        k=0
        while k<len(seq):
            if k<mid:
                left[i]=seq[k]
                i+=1
            else:
                right[j]=seq[k]
                j+=1
            k+=1
        print(left, right)
        left=mergeSort(left)
        right=mergeSort(right)

        i=0
        j=0
        k=0
        sortedSeq=[ None for _ in range(len(left)+len(right))]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                sortedSeq[k]=left[i]
                i+=1
            else:
                sortedSeq[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            sortedSeq[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            sortedSeq[k]=right[j]
            j+=1
            k+=1
        return sortedSeq
    return seq
sortedStmt = mergeSort(stmt)
print(sortedStmt)

def interpolationSearch(sortedStmt, item, start, end):
    if start<=end:
        mid=int(start+(((end-start)/(sortedStmt[end]-sortedStmt[start]))*(item-sortedStmt[start])))
        if sortedStmt[mid]==item:
            return mid
        elif sortedStmt[mid]>item:
            return interpolationSearch(sortedStmt, item, start, mid-1)
        elif sortedStmt[mid]<item:
            return interpolationSearch(sortedStmt, item, mid+1, end)
    else:
        return -1
print(interpolationSearch(sortedStmt, ele, 0, len(sortedStmt)-1))
