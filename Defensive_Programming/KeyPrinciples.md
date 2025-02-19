## Key Principles
Defensive programming is an approach to writing code where the programmer tries to anticipate problems that could affect the program and then takes steps to defend the program against these problems. Many issues could cause a program to run unexpectedly, so it's essential to write code that can handle these situations gracefully.

1. **Validate Input**: Always check user input to ensure it meets expected criteria.
2. **Handle Exceptions**: Use `try-except` blocks to catch and handle runtime errors.
3. **Use Assertions**: Add assertions to check for conditions that should always be true.
4. **Write Modular Code**: Break your code into smaller, reusable functions to isolate and manage errors.

## Example: Validating User Input
```python
def get_positive_integer():
    while True:
        try:
            value = int(input("Enter a positive integer: "))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

By following these principles, you can write code that is more robust, maintainable, and less prone to unexpected failures.
