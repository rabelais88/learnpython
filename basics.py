def main():
    print("hello!")
    # """ stands for multi-line strings
    teststr = """\
    this is how we use multi-line
    interesting, isn't it?
    why should I print it this way?
    dunno.\
    """
    print(teststr)

    # test value type conversion
    testvar = 2018
    print("this is year " + str(testvar))

    # literal expression test
    emotion = "fun"
    stuff = "literal expression"

    literal = "i'm having {emotion} with {stuff}".format(emotion=emotion,stuff=stuff)
    print(literal)

    literal2 = "i'm {0} yrs old in {1}".format(31,2018)
    print(literal2)

    userName = input("your name?")
    print("hello,", userName)
main()