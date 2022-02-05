choice = input('1:Integer\n2:Character\nEnter Choice:')
list = list(input('Enter Statement: ').split(' '))
if choice=='1':
    list = [int(s) for s in list]

def compare(list, step=1):
    i, interval = 0, len(list)//(2**step)
    print(interval)
    while i+interval<len(list):
        if list[i+interval]<list[i]:
            list[i+interval], list[i] = list[i], list[i+interval]
            j = i
            while j-interval>=0:
                if list[j]<list[j-interval]:
                    list[j], list[j-interval] = list[j-interval], list[j]
                    j-=interval
                else:
                    j=interval-1
        i+=1
    if interval > 1:
        list = compare(list, step+1)
    return list
print(compare(list))
