def find_subsets(current_subset, remaining_list, all_subsets):
    if not remaining_list:  # Base case
        all_subsets.append(current_subset)
        return
    
    # Exclude the first element
    find_subsets(current_subset, remaining_list[1:], all_subsets)

    # Include the first element
    find_subsets(current_subset + [remaining_list[0]], remaining_list[1:], all_subsets)
def generate_subsets(input_list):
    all_subsets = []
    find_subsets([], input_list, all_subsets)
    return all_subsets
# Example usage
input_list = [1, 2, 3]
print(generate_subsets(input_list))