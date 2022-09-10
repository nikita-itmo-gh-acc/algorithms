

with open("input.txt", "r") as file:
    data = file.read()
    a, b = map(int, data.split())
    res = a + b * b
    with open("output.txt", "w") as out:
        print(res, file=out)
