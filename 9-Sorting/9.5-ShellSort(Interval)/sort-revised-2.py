lst = list(map(int, input('Enter Statement: ').split()))

gap = len(lst)//2
while gap>0:
    i=0
    while i<len(lst)-gap:
        print(lst, "Gap-->>", gap, "Pointer", i, "Compared-->>", lst[i], lst[i+gap], True) if lst[i]<lst[i+gap] else print("")
        j=i
        while j>=0 and lst[j+gap]<lst[j]:
            print(lst, "Gap-->>", gap, "Pointer", j, "Compared-->>", lst[j], lst[j+gap], (False if lst[j]>lst[j+gap] else ""))
            lst[j+gap], lst[j]=lst[j], lst[j+gap]
            j-=gap
        i+=1
    gap//=2
