#Write a python program to find the second largest and second smallest element in an array.
def find_second_largest_smallest(arr):
    if len(arr) < 2:
        return None, None  # Not enough elements to find second largest and smallest

    # Remove duplicates by converting the array to a set
    unique_arr = list(set(arr))

    if len(unique_arr) < 2:
        return None, None  # Not enough unique elements to find second largest and smallest

    # Sort the unique array
    unique_arr.sort()

    # The second smallest is the second element in the sorted array
    second_smallest = unique_arr[1]

    # The second largest is the second to last element in the sorted array
    second_largest = unique_arr[-2]

    return second_largest, second_smallest

# Example usage
arr = [12, 5, 7, 3, 8, 5, 12, 9]
second_largest, second_smallest = find_second_largest_smallest(arr)

print(f"Second largest element: {second_largest}")
print(f"Second smallest element: {second_smallest}")
