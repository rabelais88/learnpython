import random
fruits = ["apple","banana","mango"]
fruits.append("kiwi")


for i in fruits:
  print(i + " is in the basket")

i = random.randint(0,len(fruits)-1)
print(fruits[i])

for i,v in enumerate(fruits):
  print(i,v)

#list extension
c = [1,2,3] + [4,5,6]
c.extend([7,8]) #extend and append play two different roles
c.append([9,10])
print(c)

#python slice doesn't need an explicit method
d = range(1,10)
e = [1,2,3,4,5,6,7,8,9,10]
print(d[0:4]) # zero can be omitted
print(d[:4])
print(e[5:])
print(e[-3:])
#range does not supprot element deletion!
del e[:4]
print('element is deleted', e)

f = ["one","two","three"] # equals to javascript's .indexOf()
print(f.index("two"))

# while they don't seem but set / list / tuple are interchangable.
# it's a concept for locking-in elements in order to do calculations
# for specific data types

a = ["horse","cat","dog"] #array(list)
b = ("horse","cat","dog") #tuple
c = {"horse","cat","dog"} #set
print(a,b,c)

a = set(a) #or tuple(a), list(b)
print(a)
a = a - {"cat"}
c = c & {"horse", "house"}
print(a,c)
d = {"a":1, "b":2,"c":5} #dictionary

#since dictionary doesn't have indexes, must use 'in' instead of .index()
print("b" in d)
print(list(d.keys()))
for i,el in enumerate(d.keys()):
  print(i,el)
for i,el in enumerate(d.values()):
  print(i,el)
for name,val in d.items():
  print(name,val)