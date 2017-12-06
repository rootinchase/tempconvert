# convert.py
# A program to convert temperatures
# by: Ryan Chase


def temp_convert_f_c(inputted):
    # This function converts fahrenheit to celsius
    temp_output = (inputted - 32) * 5/9
    return temp_output


def temp_convert_c_f(inputted):
    # This function converts celsius to fahrenheit
    temp_output = 9/5 * inputted + 32
    return temp_output


def temp_convert_c_k(inputted):
    # This function converts celsius to kelvin
    output = inputted + 273.15
    return output


def temp_convert_k_c(inputted):
    # This function converts kelvin to celsius
    output = inputted - 273.15
    return output


def temp_convert_r_f(inputted):
    # This function converts Rankine to Fahrenheit
    output = inputted + 459.67
    return output


def temp_convert_f_r(inputted):
    # This function converts fahrenheit to Rankine
    temp_output = inputted - 459.67
    return temp_output


def temp_convert_engine(temp, unit_current, unit_final):
    # this converts units two numbers that go in order of how there related
    unit_current = unit_current[0].upper()
    unit_final = unit_final[0].upper()
    if unit_current == "R":  # Rankine becomes 1, since it's at an end
        unit_current = 1
    if unit_current == "F":  # Fahrenheit becomes 2, 1 formula converts to Rankine and one Celsius
        unit_current = 2
    if unit_current == "C":  # Celsius becomes 3, one to Fahrenheit, and one to kelvin
        unit_current = 3
    if unit_current == "K":  # Kelvin is the other end
        unit_current = 4
    if unit_final == "R":
        unit_final = 1
    if unit_final == "F":
        unit_final = 2
    if unit_final == "C":
        unit_final = 3
    if unit_final == "K":
        unit_final = 4
    if unit_current > unit_final:  # if it's the same unit this won't apply
        if unit_current == 4:  # if it's kevin convert to celsius
            temp = temp_convert_k_c(temp)
            unit_current = 3

        if unit_current == 3 and unit_final != 3:  # if it's celsius and that's not the end, convert to fahrenheit
            temp = temp_convert_c_f(temp)
            unit_current = 2

        if unit_current == 2 and unit_final != 2:
            temp = temp_convert_f_r(temp)
            unit_current = 1

    elif unit_current < unit_final:  # if it's the same unit this won't apply
        if unit_current == 1:
            temp = temp_convert_r_f(temp)
            unit_current = 2

        if unit_current == 2 and unit_final != 2:
            temp = temp_convert_f_c(temp)
            unit_current = 3

        if unit_current == 2 and unit_final == 1:
            temp = temp_convert_c_f(temp)
            unit_current = 4
    # I can get away with  having no else statement
    return temp, unit_current, unit_final


def temp_convert_input():
    print("This program to convert temperatures between units")
    # this gets the user specified temperature
    temp = eval(input("What is the first temperature? "))
    # we now need to know what conversion they want
    print("What unit of temperature is this in? ")
    print('Enter "C" for Celsius, or "F" for Fahrenheit,')
    unit_start = input('or "K" for Kelvin, or "R" for Rankine: ')
    # This is to select the final unit
    print('Using the same abbreviations as before,')
    unit_end = input("What do you want this in? ")
    unit_current = unit_start[0]
    unit_final = unit_end[0]
    final_temp, unit_current, unit_final = temp_convert_engine(temp, unit_current, unit_final)
    print(temp, unit_start, "is ", final_temp, unit_end)


# it's useless to have functions, and not call on them...
temp_convert_input()
