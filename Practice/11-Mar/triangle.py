repeatuntil = int(input("Enter a number to make triangle: "))


def func(i, repeatuntil):
    i += 1

    print(str(repeatuntil) * i)

    if i <= (repeatuntil - 1):
        func(i, repeatuntil)


func(0, repeatuntil)
