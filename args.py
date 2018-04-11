def revertargs(arg1,arg2):
  msg = "arg1 = {0}, arg2 = {1}".format(arg1,arg2)
  print(msg)

revertargs(arg2=2,arg1=1)

def arbitraryArgs(*testarg): # this returns argument as array
  for i,v in enumerate(testarg):
    print(i,v)

arbitraryArgs("banana","pineapple")


def dictArgs(**testarg): # this returns argument as dictionary
  for i,v in testarg.items():
    print(i,v)

dictArgs(pellet=2,canard=50)

print((lambda x,y:x+y)(2,3))