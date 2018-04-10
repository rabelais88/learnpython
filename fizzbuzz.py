

max_val = 20

for i in range(1, max_val):
    result = ""
    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += "buzz"
    print(i, result)