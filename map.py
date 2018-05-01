x = list(range(1, 10))
print(x)

def funcmap(x):
  # it's not global because there is no global x declaration
  return x * 2
x = list(map(funcmap,x)) # == list(map(lambda target:target*2,x))
print(x)

x2 = list(range(1,30))
x2 = list(map(lambda x: "even number" if x % 2 == 0 else x, x2))
print("mapped :", x2)

x3 = list(range(1,30))
x3 = list(filter(lambda x: (x % 2) == 0, x3))
print("odd number filtered : ",x3)

cards = ["jack","queen","king"]
# this automatically gives numbers to each element
print(list(enumerate(cards)))
