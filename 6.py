def kth_smallest_element(lst, k):
    # Check if k is valid
    if k < 1 or k > len(lst):
        return "Invalid value of K"
    
    # Sort the list
    sorted_list = sorted(lst)
    
    # Return the K-th smallest element
    return sorted_list[k - 1]
