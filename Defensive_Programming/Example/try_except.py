# Example: Using try-except for Error Handling

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input types."
    else:
        return f"The result is {result}"
    finally:
        print("Execution complete.")

# Test the function
print(divide_numbers(10, 2))  # Valid input
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "a"))  # Invalid input type
