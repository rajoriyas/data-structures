choice = input('1:Integer\n2:Character\nEnter Choice:')
seq = list(input('Enter Statement: ').split(' '))
if choice=='1':
    seq = [int(s) for s in seq]

def partition(list, pivot, start):
    i, j = start, start-1
    while i<pivot:
        if list[pivot]>=list[i]:
            j+=1
            list[j], list[i] = list[i], list[j]
        i+=1
    j+=1
    list[j], list[pivot] = list[pivot], list[j]
    return list, j

def quick(list, pivot, start=0):
    """
    END PIVOT
    """
    end = pivot
    if end>start:
        list, pivot = partition(list=list, pivot=pivot, start=start)
        list = quick(list=list, pivot=pivot-1, start=start)
        list = quick(list, pivot=end, start=pivot+1)
    return list
print(quick(seq, len(seq)-1))
