def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci series are: {result}")
