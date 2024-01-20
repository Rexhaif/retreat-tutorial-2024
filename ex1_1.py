from rich import print

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

test_values = [0, 1, 5, 10]
factorials = [factorial(n) for n in test_values]
print(factorials)