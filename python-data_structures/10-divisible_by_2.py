#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]

if __name__ == "__main__":
    print(divisible_by_2([1, 2, 3, 4, 5]))
    print(divisible_by_2([0, -2, -3, -4]))
    print(divisible_by_2([]))
