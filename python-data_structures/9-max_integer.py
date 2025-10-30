#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value  # Return the biggest integer

# Example usage
if __name__ == "__main__":
    print(max_integer([1, 2, 3, 4, 5]))  # Output: 5
    print(max_integer([-1, -2, -3, -4]))  # Output: -1
    print(max_integer([]))                 # Output: None
