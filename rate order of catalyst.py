#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Input the number of arrays
# Input the number of arrays
num_arrays = int(input("Enter the number of arrays: "))

# Input array length
n = int(input("Enter the length of arrays: "))

# List to store arrays
all_arrays = []

# Input arrays
for array_num in range(1, num_arrays + 1):
    # Initialize an empty array
    my_array = []

    # Input array elements (as floating-point numbers)
    for i in range(n):
        element = float(input(f"Enter element {i + 1} of array {array_num}: "))
        my_array.append(element)

    # Append the array to the list of arrays
    all_arrays.append(my_array)

# Print all arrays
print("All arrays:", all_arrays)

# Create an array to store the mean of each index
mean_array = [sum(x) / len(all_arrays) for x in zip(*all_arrays)]

# Print the mean array
print("Mean of each index:", mean_array)


# 
# #### 

# In[ ]:





# In[ ]:




