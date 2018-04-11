

max_val = 20

for i in range(1, max_val):
    result = ""
    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += "buzz"
    print(i, result)

print("." * 30)

#fizzbuzz using list comprehension + tertiary operator
res = [
    "Fizz Buzz" if i % 15 == 0 else "Fizz"
    if i % 3 == 0 else "Buzz"
    if i % 5 == 0 else str(i)
    for i in range(1,21)
]

print("\n".join(res))