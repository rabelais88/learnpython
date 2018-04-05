x = list(range(1, 10))
print(x)

def funcmap(x):
  # it's not global because there is no global x declaration
  return x * 2
x = list(map(funcmap,x)) # == list(map(lambda target:target*2,x))
print(x)