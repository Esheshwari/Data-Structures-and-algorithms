#2.a Program to find the sum of the digits of a number using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
number = 1234
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}")


#2.b. Write a program to calculate the power of a number using recursion.
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
