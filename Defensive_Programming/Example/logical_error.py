# Example: Identifying Logical Errors

def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return "Error: The list is empty."
    return sum(numbers) / len(numbers)

# Test the function
print(calculate_average([1, 2, 3, 4, 5]))  # Valid input
print(calculate_average([]))  # Empty list
