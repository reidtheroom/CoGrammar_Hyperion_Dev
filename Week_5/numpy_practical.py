import numpy as np 

lista = [2, 4, 5, 6, 8]

# array function
numpy_array = np.array(lista)
print(numpy_array)

# zeros function
print(np.zeros(10))
print(np.zeros((5, 4)))

# arange function
print(np.arange(5))
print(np.arange(1, 10, 2))

# rand function
print(np.random.rand(10))
print(np.random.rand(10) * 100)

# N-dimensions array
print(np.array([
                [1, 2, 3],
                [4, 5, 6]
            ]))

# full function
print(np.full((2, 2), 5))
# can use with strings
print(np.full((2, 2), "Hi"))

# rand n-dimensions
print(np.random.rand(3, 4, 5) * 100)

# empty function
print(np.empty((3, 4)))

# data types
print(np.array([1, 2, 3, 4, 5]).dtype)
print(np.array([1+2j, 2+2j]).dtype)
