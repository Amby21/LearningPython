# Python Practice 3: Loops

seq = [1,2,3,4,5]

#num will hold each value inside seq for each time the loop is run.
for num in seq:
    print(num)

# Output 
# 1
# 2
# 3
# 4
# 5

#While Loops, till a certain value is reached, continue to run the code
i = 1
while i<5:
    #Code to be run till the value of i is less than 5.
    print('i is: {}'.format(i))
    #Increment the value of i by 1, so that it doesnt go into infinite loop.
    i = i + 1

# Output: 
# i is: 1
# i is: 2
# i is: 3
# i is: 4

#For Loop with Range function

for x in range(0,5):
    print(x)
# Output: 0
# 1
# 2
# 3
# 4
x = [1,2,3,4]
#List Comprehension
# It is a way to create a list in a format of calculation , loop & condition, in the below example num**2 is the calculation , the loop is for all values in x
print([num**2 for num in x])

# Output: [1, 4, 9, 16]

#To create a function: a block of code, designed to do a specific job

def square(num):
    return num**2
#Passing value to the function, in this case 2
output =  square(2)

print(output)

# output: 4