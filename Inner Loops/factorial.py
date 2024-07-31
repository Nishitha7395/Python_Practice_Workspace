#factorial.py
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is undefined for negative numbers")
elif n == 0 or n == 1:
    print(f"The factorial of {n} is 1")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial =factorial*i
    print(f"The factorial of {n} is {factorial}")