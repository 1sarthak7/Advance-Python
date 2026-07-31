def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


# Main Program
n = int(input("Enter the value of n: "))
print("Fibonacci Number =", fibonacci(n))