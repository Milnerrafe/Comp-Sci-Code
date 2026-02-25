def multiply(No1, No2):
    answer = No1 * No2
    return answer


def divide(No1, No2):
    answer = No1 / No2
    return answer


def factor(No1):
    answer = 1
    for i in range(1, No1 + 1):
        answer = answer * i

    return answer


function = input("Select Function: ")
if function == "!" or "y":
    No1 = int(input("Please Enter the First Number: "))
    if function == ("!"):
        answer = factor(No1)
        print(str(answer))
else:
    print("That input was not recognized, please try again")
