def show_func_name(func):
  def wrapper(*args, **kwargs):
    print("--- start: " + func.__name__)
    res = func(*args, **kwargs)
    print("--- end: " + func.__name__)
    return res
  return wrapper

@show_func_name
def testfunc():
  print("this is a test function")

def testfunc2():
  print("this is a test function 2")

testfunc()
testfunc2()