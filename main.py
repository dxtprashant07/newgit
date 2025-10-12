def find_median_of_union(arr1, arr2):
    # Step 1: Get the union of both arrays
    union_array = list(set(arr1) | set(arr2))  # Using set union to get unique elements from both arrays
    
    # Step 2: Sort the union array
    union_array.sort()
    
    # Step 3: Find the median
    n = len(union_array)
    if n % 2 == 1:  # If the length of the array is odd, return the middle element
        return float(union_array[n // 2])
    else:  # If the length is even, return the average of the two middle elements
        return (union_array[n // 2 - 1] + union_array[n // 2]) / 2.0

# Example usage:
arr1 = [1, 3, 8, 7]
arr2 = [2, 4, 6, 5, 8]
median = find_median_of_union(arr1, arr2)
print("Median of the union of both arrays is:", median)
