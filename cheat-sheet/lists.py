# lists
list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur']

# accessing values in Lists
print(list[0])
print(list[1:5])
print(list[3:])

# delete List Elements
del list[1]
print(list)
# or
list.remove('consectetur')

# basic List Operations
# length
len(list)

# concatenation
list = list + ['sed', 'do', 'eiusmod']
# or
list.extend(['sed', 'do', 'eiusmod'])

# repetition
list[1] * 4

# membership
print('Lorem' in list)

# iteration
for l in list:
    print(l)

# append
list.append('something')
print(list)

# insert
i = 3
list.insert(i, 'veniam')

# pop
# remove and return
list.pop(1)
list.pop() # last element

# count
print(list.count('do')) # Return the number of times x appears in the list

# sort
list.sort(reverse=True)
# def my_custom_order(elem):
#     return elem
# list.sort(key=my_custom_order)
print(list)

# reverse
list.reverse()

# shallow copy
list_copy = list.copy()
# or
list_other_copy = list[:]

# clear
list.clear() # remove all
