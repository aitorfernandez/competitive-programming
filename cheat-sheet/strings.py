string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'

# string length
print(len(string))

# iterate
for c in string:
    print(c)

# iterate with enum
for i, c in enumerate(string):
    print(i, c)

# reversed string
print(''.join(reversed(string)))

# slicing
print(string[:11])   # Lorem ipsum
print(string[:11:2]) # Lrmism
print(string[-4:])   # elit

# count the number of times appear
print(string.count('o'), string.count('dolor'))

# position
print(string.find('sit'), string.find('o', 5)) # find after fifth character
print(string.find('consectetur', 25, -6))      # find backwards, between t, <-> ng eli

# replace
print(string.replace('o', 'e'))

# replace in range
print(string[:10].replace('o', 'e') + string[10:])

# uppercase
print(string.upper())

# lowercase
print(string.lower())
