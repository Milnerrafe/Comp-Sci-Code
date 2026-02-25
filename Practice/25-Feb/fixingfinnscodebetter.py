def getinput(numeberofnumbers):
    match numeberofnumbers:
        case 1:
            number_input_1 = int(input("Please Enter the Number: "))
            return [number_input_1]
        case 2:
            number_input_1 = int(input("Please Enter the First Number: "))
            number_input_2 = int(input("Please Enter the Second Number: "))
            return [number_input_1, number_input_2]


def multiply(number1, number2):
    answer = number1 * number2
    return answer


def divide(number1, number2):
    answer = number1 / number2
    return answer


def factor(number1):
    answer = 1
    for i in range(1, number1 + 1):
        answer = answer * i

    return answer


print("Welcome to MathScript, press control + C,any time to exit")
function_input = input("Choose a function, *, !, +, -, /, s(√): ")

match function_input:
    case "*":
        input_numbers = getinput(2)
        print(
            f"Your answer is, {multiply(int(input_numbers[0]), int(input_numbers[1]))}"
        )

    case "!":
        input_numbers = getinput(1)
        print(f"Your answer is, {factor(int(input_numbers[0]))}")

    case "/":
        input_numbers = getinput(2)
        print(f"Your answer is, {divide(int(input_numbers[0]), int(input_numbers[1]))}")

    case "+":
        print("Sorry, this functionality hasn't been added yet.")

    case "-":
        print("Sorry, this functionality hasn't been added yet.")

    case "s":
        print("Sorry, this functionality hasn't been added yet.")

    case _:
        print("That input was not recognized, please try again")
