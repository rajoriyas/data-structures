seq=list(map(int, input('Enter Statement: ').split()))

def quickSort(seq, start, end):
    if start<end:
        i=start-1
        j=start
        pivot=end
        """
        these two condition `j==end and seq[j]==seq[pivot]` are used below  to put pivot element from last to i+1 position,
        as we used to do seperatly at the end to while loop.
        """
        while j<=end:
            if seq[j]<=seq[pivot]:
                i+=1
                seq[i], seq[j]=seq[j], seq[i]
                print(seq[start:end+1], i, seq[pivot])
            j+=1
        seq=quickSort(seq, start, i-1)
        seq=quickSort(seq, i+1, end)
    return seq
print(quickSort(seq, 0, len(seq)-1))
