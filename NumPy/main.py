import numpy as np

# numpy array

my_list = [10,20,30]
print(type(my_list))

np.array(my_list)

my_numpy_aray = np.array(my_list)
print(my_numpy_aray)

print(my_numpy_aray[0])
print(my_numpy_aray[-1])

my_numpy_aray [0] = 100
print(my_numpy_aray[0])

print("\n")

print(my_numpy_aray.max())
print(my_numpy_aray.min())
print(my_numpy_aray.mean())

matrix_list = ((1,0,0),(0,1,0),(0,0,0))
print(matrix_list[0][0])

numpy_matrix_list = np.array(matrix_list)
print(np.array((matrix_list)))

numpy_matrix_list.shape
print(numpy_matrix_list.shape)

print(list(range(1,10)))

print(np.arange(0,10))
# numpy dizisi olarak oluşturur.

print(np.arange(0,10,2))

print(np.ones((10,10)))

print("\n")

print(np.zeros((10,10)))

print(np.linspace(0,10,10))

print(np.random.randint(1,10,3))
print(np.random.randint(1,15,2))

#numpy arrays methods

my_numpy_list = np.arange(0,20)
print(my_numpy_list)

print(my_numpy_list[4:9:2])
my_numpy_list [4:9:2] = -10

print(my_numpy_list[4:9:2])

other_list =np.arange(0,15)
other_list[4:10]
slicing_list = other_list[4:10]
print(slicing_list)
slicing_list[:] = 100
print(slicing_list)

print(other_list)

numpy_list_3 = np.arange(0,20)
numpy_list_3_copy = numpy_list_3.copy()
print(numpy_list_3)
print(numpy_list_3_copy)

slicing_3 = numpy_list_3_copy[4:9]
print(slicing_3)
slicing_3[:] = -100
print(numpy_list_3)
print(slicing_3)

#NUMPY operations
print("\n\n\n")
new_array = np.random.randint(1,150,25)
print(new_array)

print(new_array>50)

result_array = new_array>50

new_array[result_array]
print(new_array[result_array])

last_array = np.arange(0,30)
print(last_array+last_array)
print(last_array*last_array)
print(last_array-last_array)
#last_array.max() = np.max(last_array

np.sqrt(last_array)
print(np.sqrt(last_array))

