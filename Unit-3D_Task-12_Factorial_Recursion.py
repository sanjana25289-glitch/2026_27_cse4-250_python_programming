def factorial(k):
    if k == 0:
        return 1
    return k * factorial(k - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")
