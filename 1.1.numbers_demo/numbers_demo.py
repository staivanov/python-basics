# 1. Basic arithmetic operations
number_a: int = 2
number_b: int = 3
sum_of_number_a_and_b: int = number_a + number_b
print("sum: ", sum_of_number_a_and_b)
subtracted_numbers: int = 5 - 1
print("subtracted numbers", subtracted_numbers)
numbers_multiplication: int = 6 * 2
print("numbers multiplication", numbers_multiplication)
numbers_division: float | int = 9 / 3
print("numbers division", numbers_division)
numbers_exponents: int = 3 ** 3
print("numbers exponents: ", numbers_exponents)

# 2. Dividing two integers
number_one: int = 9
number_two: int = 3
two_numbers_divided: float | int = number_one / number_two
print("two numbers divided :", two_numbers_divided)

print('*' * 40)

# 3. Basic arithmetic operations between int and float numbers
n1: int = 6
n2: float = 2.0
print("Numbers for next demo where one is int and other is float are ", n1, "and", n2)
print("Int number plus float number is: ", n1 + n2)
print("Int number multiplied by float is: ", n1 * n2)
print("Float number pow on int number is: ", n2 ** n1)

# 4. Multiple Assignment
x, y, z = 0, 0, 0  # type: int, int, int

# 5. Constants
MAX_POWER: int = 220
MIN_POWER: int = 120
