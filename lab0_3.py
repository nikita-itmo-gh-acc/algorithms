

Fib = [0] * (10**7 + 1)
Fib[0], Fib[1] = 0, 1
with open("input.txt", "r") as file:
    n = int(file.read())
    if n >= 2:
        for i in range(2, n + 1):
            Fib[i] = (Fib[i - 1] + Fib[i - 2]) % 10
    with open("output.txt", "w") as out:
        print(Fib[n], file=out)