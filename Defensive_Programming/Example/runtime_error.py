# Example: Handling Runtime Errors

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range."

# Test the function
my_list = [1, 2, 3]
print(access_list_element(my_list, 1))  # Valid index
print(access_list_element(my_list, 5))  # Out-of-range index
