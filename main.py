from loops import *
from recursion import *

# print("Factorial of 6 using a loop is:", loops.factorial(6))
# print("Factorial of 5 using a loop is:", loops.factorial(5))
# print("Factorial of 1 using a loop is:", loops.factorial(1))

# print("Factorial of 6 using recursion is:", recursion.factorial(6))
# print("Factorial of 5 using recursion is:", recursion.factorial(5))
# print("Factorial of 1 using recursion is:", recursion.factorial(1))

# print("2 to the 5th power using a loop is:", loops.power(2, 5))
# print("2 to the 4th power using a loop is:", loops.power(2, 4))
# print("2 to the 0 power using a loop is:", loops.power(2, 0))

# print("2 to the 5th power using recursion is:", recursion.power(2, 5))
# print("2 to the 4th power using recursion is:", recursion.power(2, 4))
# print("2 to the 0 power using recursion is:", recursion.power(2, 0))



def recursionTest():
    numbers = list(map(int, input("Enter seven numbers separated by a space: ").split()))
    start_index = int(input("Enter the index at which the search will begin: "))
    search_size = int(input("Enter the size of the list that will be searched: "))
    target_value = int(input("Enter the target value to search for: "))

    result = recursion.recursive_search(numbers, start_index, search_size, target_value)

    if result != -1:
        print(f"Target found at index ... {result}")
    else:
        print(f"{target_value} not found.")

recursionTest()