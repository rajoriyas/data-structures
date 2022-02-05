statement = list(input('Statement:').split(' '))
ele = input('Element:')
found, loc = False, -1
#new way of for loop
for index, item in enumerate(statement):
    if item == ele:
        loc = index
 	found = True
if found:
	print('Element found at', loc)
else:
	print('Element not found')
