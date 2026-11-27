arr = [1,2,3,4]

for i in range(len(arr)): # Alternative: for i in arr[:]: to avoid modifying the list while iterating
   arr.remove(arr[i])  # This will cause an IndexError because the list is being modified while iterating over it
   # Alternative: arr.remove(i) to remove the current element instead of using the index
print(arr)  # Output: [2, 4], because the loop skips elements due to the removal of items