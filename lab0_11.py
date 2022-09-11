import time

start = time.perf_counter()
with open("input.txt", "r") as file:
    data = file.read()
    a, b = map(int, data.split())
    res = a + b
    with open("output.txt", "w") as out:
        print(res, file=out)
        print(time.perf_counter() - start)
