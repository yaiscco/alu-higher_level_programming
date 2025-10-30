#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list

if __name__ == "__main__":
    print(delete_at([1, 2, 3, 4], 2))
    print(delete_at([10, 20, 30], 0))
    print(delete_at([5, 6, 7], 5))
    print(delete_at([9], -1))
