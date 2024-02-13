n = int(input("Enter a number: "))

fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)
fib_series = [fib(i) for i in range(n)]

print(f"Fibonacci series up to {n}:",fib_series)

