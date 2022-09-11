import time

start = time.perf_counter()
Fib = [0] * 50
Fib[0], Fib[1] = 0, 1
with open("input.txt", "r") as file:
    n = int(file.read())
    if n >= 2:
        for i in range(2, n + 1):
            Fib[i] = Fib[i - 1] + Fib[i - 2]
    with open("output.txt", "w") as out:
        print(Fib[n], file=out)
        print(time.perf_counter() - start)

