
def bumper(func):
  def wrapper(*args,**kwargs):
    print("*" * 30)
    res = func(*args, **kwargs)
    print("*" * 30)
    return res
  return wrapper

@bumper
def draw_menu(menus):
  for i, el_menu in enumerate(menus):
    print("{0} --- {1}".format(i, el_menu))


def main():
  menu = ["menu" + str(i) for i in range(1,4)]
  menu.append("quit")

  is_run = True
  while is_run:
    draw_menu(menu)
    chosen = input("choose your menu>>")
    try:
      chosen = int(chosen)
      if chosen == len(menu) - 1:
        print("exit")
        is_run = False # == sys.exit(0)
      else:
        print("--->menu chosen {0}".format(menu[chosen]))
    except Exception as e:
      print("wrong input!")

main()
