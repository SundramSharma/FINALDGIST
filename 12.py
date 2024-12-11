def quick_sort(lst):
    # Base case: a list of length 0 or 1 is already sorted
    if len(lst) <= 1:
        return lst
    
    # Choose the pivot (we will use the last element)
    pivot = lst[-1]
    
    # Partition the list into two sublists: less than pivot and greater than pivot
    left = [x for x in lst[:-1] if x <= pivot]
    right = [x for x in lst[:-1] if x > pivot]
    
    # Recursively apply quick_sort to left and right, and combine with pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
unsorted_list = [7, 10, 4, 3, 20, 15]
sorted_list = quick_sort(unsorted_list)
print(sorted_list)  # Output: [3, 4, 7, 10, 15, 20]
