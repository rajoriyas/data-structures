stmt = list(map(int, input('Statement:').split()))
ele = int(input('Element:'))

def quickSort(seq, start, end):
    if start<end:
        i=start-1
        j=start
        pivot=end
        while j<=end:
            if seq[pivot]>=seq[j]:
                i+=1
                temp=seq[j]
                seq[j]=seq[i]
                seq[i]=temp
            j+=1
        quickSort(seq, start, i-1)
        quickSort(seq, i+1, end)
    return seq
sortedStmt = quickSort(stmt, 0, len(stmt)-1)
print(sortedStmt)

def binarySearch(sortedStmt, item, start, end):
    if start<=end:
        mid=(start+end)//2
        if sortedStmt[mid]==item:
            return mid
        elif sortedStmt[mid]>item:
            return binarySearch(sortedStmt, item, start, mid-1)
        elif sortedStmt[mid]<item:
            return binarySearch(sortedStmt, item, mid+1, end)
    else:
        return -1
print(binarySearch(sortedStmt, ele, 0, len(sortedStmt)-1))
