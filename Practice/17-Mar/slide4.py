userInput = int(input("Enter a number between 1 and 100:  "))


if userInput > 1 and userInput < 100:
    if userInput % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("Number out of range!")
