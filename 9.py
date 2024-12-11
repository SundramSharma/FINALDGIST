def reverse_list(lst):
    # Base case: If the list is empty or has one element, return it
    if len(lst) <= 1:
        return lst
    # Recursive case: Reverse the rest and append the first element at the end
    return [lst[-1]] + reverse_list(lst[:-1])
