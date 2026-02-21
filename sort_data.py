import numpy as np

data = np.genfromtxt('sample_data.csv', delimiter=',', skip_header=1)

print("Original data:")
print(data)

print("\nSorted by first column (ascending):")
print(np.sort(data, axis=0))

print("\nSorted by first column (descending):")
print(np.sort(data, axis=0)[::-1])
