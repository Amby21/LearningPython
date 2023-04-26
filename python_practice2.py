#Python practice 2

d = {'key1':'value','key2':123}
d['key1']
# Output: 'value'
dict = {'k1':[1,2,3]}

lst = dict['k1']

print(lst)
# Output: [1,2,3]

d = {'k1':{'innerkey':[1,2,3]}}
print(d['k1']['innerkey'])
# Output: [1, 2, 3]

my_list  = [1,2,3]

t = (1,2,3)

my_set = {1,2,3}

#Sets : are a collection of unique elements
print(set([1,1,1,2,2,2,5,5,5,6,6,6]))
# Output: {1, 2, 5, 6}

#comaprison Operators

print(1>2)
# Output: False

#comparison operators can be used to compare strings
print('hi' != 'bye')
# Output False

print((1<2) or (2>3) or (1==1))

# Output True

# Conditional Statements

if 1<2:
    print('Yes!')
elif 4==4:
    print('Equal!')
else:
    print('No')

# Output: Yes