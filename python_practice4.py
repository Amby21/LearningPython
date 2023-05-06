#Python Practice 4

#Map Function

seq = [1,2,3,4,5]

list(map(lambda num: num*3,seq))

list(filter(lambda num:num%2 == 0,seq))

#Dictionary
dct = {'k1': 1, 'k2': 2}
dct.keys()
dct.items()

#Lists

lst = [1,2,3,4,5]

#Removing elements from a list using pop function  
item = lst.pop()

print(item)

print(lst)

#Output
# 5
# [1, 2, 3, 4]

#Removing element by index number
first = lst.pop(0)

print(first)
#Output
# 1

#Append a new item at the end of the list
lst.append('new')
print(lst)

#Output
# [2, 3, 4, 'new']

#Tuple unpacking
x = [(1,2),(3,4),(5,6)]

for item in x:
    print(item)

# Output:
# (1, 2)
# (3, 4)
# (5, 6)
