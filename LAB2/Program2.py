#Write a program to find the factorial of a number using recursion 
def factorial(n): 
 if n == 0 or n == 1: 
 return 1 
 else: 
 return n * factorial(n - 1) 
# Example usage: 
number = 5 
result = factorial(number) 
print(f"Factorial of {number} is {result}") 

#Write a program to find the nth fibonacci number using recursion. 
def fibonacci(n): 
 if n == 0: 
 return 0 
 elif n == 1: 
 return 1 
 else: 
 return fibonacci(n - 1) + fibonacci(n - 2) 
# Example usage: 
number = 6 
result = fibonacci(number) 
print(f"The {number}th Fibonacci number is {result}") 
