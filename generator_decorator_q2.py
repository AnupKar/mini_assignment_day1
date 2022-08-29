# Create a generator to return the fibonnaci sequence starting from the first element up to (n)
a = int(input('Give amount: '))
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
print(list(fib(a)))