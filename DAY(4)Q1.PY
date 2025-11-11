#Dictionary Key/Value Swap
def swap_dict(original_dict):
    """Swaps keys and values in a dictionary."""
    new_dict = {value: key for key, value in original_dict.items()}
    return new_dict

# Test Case
d = {'a': 1, 'b': 2, 'c': 1}
print(f"2. Original: {d}, Swapped: {swap_dict(d)}")