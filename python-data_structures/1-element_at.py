#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


# Example usage
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print(element_at(my_list, 2))  # Output: 30
    print(element_at(my_list, -1))  # Output: None
    print(element_at(my_list, 5))   # Output: None
