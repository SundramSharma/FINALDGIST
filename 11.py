class UniqueItemsSet:
    def __init__(self):
        """Initialize an empty set to store unique items."""
        self.items = set()

    def add_item(self, item):
        """Add an item to the set. Ensure no duplicates."""
        self.items.add(item)

    def get_items(self):
        """Return the current set of unique items."""
        return self.items

    def count_items(self):
        """Return the count of unique items."""
        return len(self.items)

# Example 1
unique_set = UniqueItemsSet()
unique_set.add_item(10)
unique_set.add_item(20)
unique_set.add_item(10)
print(unique_set.get_items())  # Output: {10, 20}
print(unique_set.count_items())  # Output: 2

# Example 2
unique_set = UniqueItemsSet()
unique_set.add_item("apple")
unique_set.add_item("banana")
unique_set.add_item("apple")
unique_set.add_item("orange")
print(unique_set.get_items())  # Output: {'apple', 'banana', 'orange'}
print(unique_set.count_items())  # Output: 3
