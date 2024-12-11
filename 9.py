def find_median(lst):
    # Step 1: Sort the list
    lst.sort()
    
    # Step 2: Find the median
    n = len(lst)
    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle element
        return float(lst[n // 2])
    else:
        # If the list has an even number of elements, return the average of the two middle elements
        mid1 = lst[n // 2 - 1]
        mid2 = lst[n // 2]
        return (mid1 + mid2) / 2.0

# Example usage:
input_list = [7, 2, 1, 6, 8]
median = find_median(input_list)
print(median)  # Output: 6.0
