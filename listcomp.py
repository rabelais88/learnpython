# this is not spread syntax of JS ES2016
#python spread equivalent is [...x] -> [**x]

#JS implements List comprehension via Babel

#the below equals:
#data = []
#for i in range(1,6):
#  data.append(i*2)
data = [i*2 for i in range(1,6)]
print(data)
#replaceable with map lambda
# == list(map(lambda x:x*2, range(1,6)))

#nested list comprehension
base = range(1,4)
data = [(x,y) for x in base for y in base]
print(data)

data = [(x,y) for x in base for y in base if x != y]
print(data)


#creating dictionary with list comprehension
# key : value   other operators
print({"var"+str(x) : x*5   for x in range(1,4)})