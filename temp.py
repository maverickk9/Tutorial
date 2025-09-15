import numpy as np
import pandas as pd

dogs = np.array(["Pup", "Jak", "Lou"])

for dog in dogs:
    print(dog)
    
    
digits = np.array([1, 2, 3, 4, 5])
for digit in digits:
    print(digit)
    
# Operations

total = np.sum(digits)
average = np.mean(digits)

print("Sum:", total)
print("average:", average)


reshaped_dig = digits.reshape(5,1)
print("Original:", digits)
print("Reshaped:", reshaped_dig)

data = data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

print(data)

df = pd.DataFrame(data)
print(df.head())

print(df.info())