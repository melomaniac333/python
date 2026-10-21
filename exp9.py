#Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions
import  numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)

#
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#
import numpy as np

arr = np.array([10, 25, 5, 40, 15, 30, 20, 35, 50, 45])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))

#
import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)

#
import numpy as np

arr = np.arange(1, 13)

print("Original Array:")
print(arr)

print("\n2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("\n3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("\n4 x 3 Matrix:")
print(arr.reshape(4, 3))

#
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix Addition:")
print(a + b)

#
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[1, 2],
              [3, 4],
              [5, 6]])

result = np.matmul(a, b)

print("Matrix Multiplication:")
print(result)

#
import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Original Matrix:")
print(a)

print("Transpose:")
print(a.T)

#
import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("First row:", a[0])
print("Last column:", a[:, -1])
print("Diagonal:", np.diag(a))
print("Second and third rows:")
print(a[1:3])

#
import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Sum of each row:", np.sum(a, axis=1))
print("Sum of each column:", np.sum(a, axis=0))

#
import numpy as np

a = np.arange(1, 21)

print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate elements:", a[::2])
print("Reverse:", a[::-1])

#
import numpy as np

a = np.array([10, 25, 60, 45, 75, 30, 90, 15, 55, 40])

a[a > 50] = 0

print(a)

#
import numpy as np

a = np.array([50, 10, 40, 20, 30])

print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])

#
import numpy as np

a = np.array([10, 20, 10, 30, 20, 40, 30, 50])

print("Unique elements:", np.unique(a))

#
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal:")
print(np.hstack((a, b)))

print("Vertical:")
print(np.vstack((a, b)))

#
import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 78])

print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

#
import numpy as np

marks = np.array([45, 67, 89, 34, 76, 90, 55, 82, 61, 73,
                  48, 95, 70, 58, 84, 39, 66, 91, 52, 77])

average = np.mean(marks)

print("Class Average:", average)
print("Marks above average:")
print(marks[marks > average])

#
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(a)

print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)

#
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", a[0, 0, 0])
print("Last element:", a[1, 2, 3])
print("Element at [0,1,2]:", a[0, 1, 2])
print("Element at [1,2,3]:", a[1, 2, 3])

#
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of all elements:", np.sum(a))

print("Sum of each layer:")
print(np.sum(a, axis=(1, 2)))

print("Sum along rows:")
print(np.sum(a, axis=2))

print("Sum along columns:")
print(np.sum(a, axis=1))

#
import numpy as np

a = np.random.randint(1, 101, (2, 3, 4))

print("Original Array:")
print(a)

a[a > 50] = 0

print("After replacing:")
print(a)

#
import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

print("Array:")
print(a)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

#
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:")
print(a)

b = a.flatten()

print("Flattened Array:")
print(b)

#
import numpy as np

a = np.arange(1, 28).reshape(3, 3, 3)

b = a.flatten()

print("Flattened Array:")
print(b)

print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))

#
import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

b = a.flatten()

print("Flattened Array:")
print(b)

print("Greater than 50:")
print(b[b > 50])

print("Even numbers:")
print(b[b % 2 == 0])

average = np.mean(b)

print("Average:", average)
print("Less than average:")
print(b[b < average])

