#Python Crash Course 1:
#Addition
1 + 1
#output: 2

#mutiplication
1 * 3
#output: 3

#For exponent : to the power of 

2 ** 4
#Output 16

2 + 3 * (5+5)
#Output 32

#Modulus or Remainder
5%2
#Output 1

8%2
#output 0

#variable assignment
var = 2

print(var)

#output: 2
var = var + var 

print(var)
# Output: 4

#Strings
'single quote string'

num = 21
name = 'Skandan'


print('My number is {} and my name is {}'.format(num,name))

# output: My number is 21 and my name is Skandan

#Targetting elements in a string, use the index number from 0 for the first element 
#In order to get o in the word hello
s = 'hello'

print(s[4])

# Output : o
# Capturing a range of elements would require the start element, the end element and the range symbol :

print(s[0:3])
# Output: hel
# To capture all elements from the 0th index

print(s[0:])
# Output : hello

#to capture all values one before a given index
print(s[:3])
# Output: hel

#Lists
my_list = ['a','b','c']

#Insert new elements in a list
my_list.append('d')
print(my_list)
# output : ['a', 'b', 'c', 'd']

#Slicing a list is similar to slicing a string
print(my_list[1:3])
# Output: ['b', 'c']

# Assigning a element to a particular index
my_list[0] = 'NEW'
print(my_list)
# Output : ['NEW', 'b', 'c', 'd']

#Nested List: A list inside a list becomes an item for the outer list

nested = [1,2,[3,4]]

print(nested[2][1])

# Output : 4







