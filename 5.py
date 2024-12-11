def merge_and_sort_keys(dict1, dict2):
    # Merge the two dictionaries
    dict1.update(dict2)
    
    # Get all keys and sort them
    sorted_keys = sorted(dict1.keys())
    
    return sorted_keys
