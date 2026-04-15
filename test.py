def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Target not found in the array

# Example usage:
arr = [1, 2, 2, 2, 3]
target = 2

result = binary_search(arr, target)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the array")