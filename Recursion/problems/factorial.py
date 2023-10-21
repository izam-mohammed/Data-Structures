def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


for i in range(10):
    print(f"factorial {i} = {factorial(i)}")
