def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number for which factorial needs to be calculated from the user
number = int(input("Enter a number: "))

# Calculate the factorial and print the result
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    fact = factorial(number)
    print(f"Factorial of {number} is {fact}")

