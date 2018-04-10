def draw_menu(menus):
    for i, el_menu in enumerate(menus):
        print("{0} --- {1}".format(i, el_menu))


def main():
    menu = ["menu1", "menu2", "menu3"]

    is_run = True
    while is_run:
        draw_menu(menu)
        chosen = input("choose your menu>>")
        chosen = int(chosen)
        if chosen == 1:
            print("you have chosen 1!")
        elif chosen == 2:
            print("this is number 2!")
        else:
            print("wtf")
            is_run = False


main()
