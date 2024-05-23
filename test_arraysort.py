def find_largest_4(arr):
    # Sort the array in descending order and select the first 4 elements
    largest_4 = sorted(arr, reverse=True)[:4]
    return largest_4

# Example usage
arr = [5, 1, 8, 7, 2, 6, 3, 4, 10, 9]
print(find_largest_4(arr))
