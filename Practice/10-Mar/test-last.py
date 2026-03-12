repeatuntil = 700


def func(i, repeatuntil):
    i += 1

    print(f"Hi, the number is {i}")

    if i <= (repeatuntil - 1):
        func(i, repeatuntil)


func(0, repeatuntil)
