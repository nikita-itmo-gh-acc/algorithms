import time
import psutil

start = time.perf_counter()
with open("input.txt", "r") as file:
    data = file.read()
    a, b = map(int, data.split())
    res = a + b * b
    with open("output.txt", "w") as out:
        print(res, file=out)
        print("exec time:", time.perf_counter() - start, file=out)
        print("memory spending (mb):", psutil.Process().memory_info().rss / (1024 * 1024), file=out)
