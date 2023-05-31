# numpy_practice1

#Vectors are 1-d Arrays and Matrices are 2-D Arrays.

my_list = [1,2,3]

#Importing Numpy Package
import numpy as np

#Casting list as Array
arr = np.array(my_list)
# print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]

np.array(my_mat)

# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

np.arange(0,10)

# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(np.zeros((2,3)))

# [[0. 0. 0.]
#  [0. 0. 0.]]

print(np.ones((3,4)))

# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

print(np.random.rand(5))
# [0.43422176 0.51509    0.59682271 0.45304015 0.38509173]

#Indexing in Array

arr = np.arange(0,11)

print(arr)

# [ 0  1  2  3  4  5  6  7  8  9 10]

print(arr[8])

# 8
#Slicing array values

print(arr[1:5])

#O/P [1 2 3 4]

#broadcast on the array

slice_of_arr = arr[0:6]

slice_of_arr[:] = 99

print(slice_of_arr)
#O/P [99 99 99 99 99 99]

#Copy an array 
copy_of_arr = arr.copy()

print(copy_of_arr)

#O/P [99 99 99 99 99 99  6  7  8  9 10]

copy_of_arr[:] = 100

print(copy_of_arr)

# O/P [100 100 100 100 100 100 100 100 100 100 100]

#numpy Indexing and Selection

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

print(arr_2d)
#O/P
# [[ 5 10 15]
#  [20 25 30]
#  [35 40 45]]

print(arr_2d[1:,1:])

# [[25 30]
#  [40 45]]

new_arr = np.arange(0,11)

print(new_arr)
# [ 0  1  2  3  4  5  6  7  8  9 10]

#Conditional Statements in Array



copy_of_arr = arr.copy()

# [99 99 99 99 99 99  6  7  8  9 10]
# [100 100 100 100 100 100 100 100 100 100 100]
# [[ 5 10 15]
#  [20 25 30]
#  [35 40 45]]



new_arr = np.arange(0,11)

# [ 0  1  2  3  4  5  6  7  8  9 10]
# [False False False False False False  True  True  True  True  True]

bool_arr = new_arr > 5

print(bool_arr)

print(new_arr[bool_arr])

# [ 6  7  8  9 10]

# NumPy Operations

arr_num = np.arange(0,11)

print(arr_num)
# [ 0  1  2  3  4  5  6  7  8  9 10]

arr_num = arr_num + 100
print(arr_num)
# [100 101 102 103 104 105 106 107 108 109 110]

arr_num = arr_num ** 2

#Square root of all elements
np.sqrt(arr_num)

arr_num.max()


