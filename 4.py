def max_depth(nested_list):
    # Base case: if it's not a list, depth is 0
    if not isinstance(nested_list, list):
        return 0

    # Initialize max_depth
    max_depth_value = 0

    # Iterate through each element in the list
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            # Recursively calculate the depth of the sublist
            max_depth_value = max(max_depth_value, max_depth(element))

    # Add 1 for the current level
    return max_depth_value + 1
