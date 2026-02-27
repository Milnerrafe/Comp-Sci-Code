def function():
    print("This is a funtion")


def function_two(parameters, are_placehoders):
    are_placehoders = (
        are_placehoders
        + "They do not have to be used in the funtion, but when the funtion is called all parameters must be past in."
    )

    p1_as_a_number = int(parameters)
    print(f"The output is {p1_as_a_number * p1_as_a_number}")


def function_three(parameter_number_1, parameter_number_2):
    output = parameter_number_1 * parameter_number_2

    print("Funtions can return vaules")

    return output


print(f"The output of function_three is, {function_three(6, 7)}")
