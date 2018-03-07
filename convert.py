# convert.py
# A program to convert temperatures
# by: Ryan Chase


def temp_convert_f_c(fahrenheit):
    # This function converts Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def temp_convert_c_f(celsius):
    # This function converts Celsius to Fahrenheit
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit


def temp_convert_c_k(celsius):
    # This function converts Celsius to Kelvin
    kelvin = celsius + 273.15
    return kelvin


def temp_convert_k_c(kelvin):
    # This function converts Kelvin to Celsius
    celsius = kelvin - 273.15
    return celsius


def temp_convert_r_f(rankine):
    # This function converts Rankine to Fahrenheit
    fahrenheit = rankine + 459.67
    return fahrenheit


def temp_convert_f_r(fahrenheit):
    # This function converts Fahrenheit to Rankine
    rankine = fahrenheit - 459.67
    return rankine


def temp_convert_engine(temp, unit_current, unit_final):
    # this converts unit codes to numbers that go in order of how there related
    # And is the "Heart" of this program.
    # you can call upon it to do the conversions for you.
    unit_current = unit_current[0].upper()  # turn it to an uppercase Char
    unit_final = unit_final[0].upper()  # turn it to an uppercase Char

    # Now change them to numbers that show the direction and order the unit will get converted.
    # Rankine and Kelvin only have one possible conversion that is applied to them, they are the "ends"
    # that are valued at 1 and 4 respectively.
    # Fahrenheit will be 2, because you can convert it to of from Rankine and Celsius with a single conversion.
    # Celsius will be 3, because you can convert it to of from Kelvin and Celsius with a single conversion.
    # Kelvin is 4 because it's the other end.
    # Now let's convert the current unit
    
    if unit_current == "R":                         # See above for what's going on
        unit_current = 1        
    elif unit_current == "F":   
        unit_current = 2        
    elif unit_current == "C":   
        unit_current = 3        
    elif unit_current == "K":   
        unit_current = 4

    # Let's repeat those code and convert the final unit for the final unit
    if unit_final == "R":
        unit_final = 1
    elif unit_final == "F":
        unit_final = 2
    elif unit_final == "C":
        unit_final = 3
    elif unit_final == "K":
        unit_final = 4

    # let's first convert from Kelvin, an SI unit based on absolute zero to Rankine,
    # an Imperial unit also based on absolute zero, while going through the other units.

    if unit_current > unit_final:  # if it's the same unit this won't apply
        # Once we're in here, unit_current will be used to track what the current unit is.

        if unit_current == 4:                       # If the current unit is Kelvin, convert it to Celsius.
                                                    # We won't encounter any conversions, where Kelvin is the end.
            temp = temp_convert_k_c(temp)           # Convert it to Celsius and store it to the variable temp.
            unit_current = 3                        # Make it to where the current unit tracker reflects Celsius.

        if unit_current == 3 and unit_final != 3:   # If it's Celsius and that's not the end, convert to fahrenheit.
            temp = temp_convert_c_f(temp)           # Converts Celsius to Fahrenheit and store it to the variable temp.
            unit_current = 2                        # Make it to where the current unit tracker reflects Fahrenheit.

        if unit_current == 2 and unit_final == 1:   # If it's Fahrenheit, and the final unit is Rankine,
                                                    # convert it to Rankine.
            temp = temp_convert_f_r(temp)           # Converts Fahrenheit to Rankine and store it to the variable temp.
            unit_current = 1                        # Make it to where the current unit tracker reflects Rankine.

        # If it goes through here, unit_current will equal unit_final,
        # which will make it not go through the other conversions.

    # Let's now convert from Rankine, an Imperial unit also based on absolute zero, to  Kelvin,
    # an SI unit based on absolute zero, while going through the other units.

    if unit_current < unit_final:  # if it's the same unit this won't apply

        if unit_current == 1:                       # if the current unit is Rankine, convert it to Fahrenheit.
            temp = temp_convert_r_f(temp)           # Converts Rankine to Fahrenheit and store it to the variable temp
            unit_current = 2                        # Make it to where the current unit tracker reflects Fahrenheit

        if unit_current == 2 and unit_final != 2:   # If the current unit is Fahrenheit, and that isn't the final unit,
                                                    # Convert it to Celsius.

            temp = temp_convert_f_c(temp)           # Convert it to Celsius and store it to the variable temp
            unit_current = 3                        # make it to where the current unit tracker reflects Celsius

        if unit_current == 3 and unit_final == 1:   # If the current unit is Celsius, and Kelvin is the final unit,
                                                    # convert it to Kelvin.
            temp = temp_convert_c_k(temp)           # Convert it to Kelvin and store it to the variable temp

    # I can get away with  having no else statement
    # because temp was the original parameter and
    # it gets reassigned during each conversion.

    return temp


def temp_convert_input():
    # This is a simple UI done in the Python console.
    # Let them know what we're doing.
    print("This program to convert temperatures between units")
    # This will get the user specified temperature and store it to the variable temp.
    temp = eval(input("What is the first temperature? "))
    # We will discover what that temperature is in, and store it to unit_start.
    print("What unit of temperature is this in? ")
    print('Enter "C" for Celsius, or "F" for Fahrenheit,')
    unit_start = input('or "K" for Kelvin, or "R" for Rankine: ')
    # Now we find out what they want it to be converted into, and stores it to unit_end
    print('Using the same abbreviations as before,')
    unit_end = input("What do you want this in? ")
    # now we will duplicate them, to make sure wee keep them intact
    unit_current = unit_start.upper()[0]
    unit_final = unit_end.upper()[0]
    final_temp = temp_convert_engine(temp, unit_current, unit_final)

    if unit_current == "R":
        unit_start = "Rankine"
    elif unit_current == "F":
        unit_start = "Fahrenheit"
    elif unit_current == "C":
        unit_start = "Celsius"
    elif unit_current == "K":
        unit_start = "Kelvin"

    if unit_final == "R":
        unit_end = "Rankine"
    elif unit_final == "F":
        unit_end = "Fahrenheit"
    elif unit_final == "C":
        unit_end = "Celsius"
    elif unit_final == "K":
        unit_end = "Kelvin"

    print(temp, " ", unit_start, " is ", final_temp, " ", unit_end)


# This will make the UI show up
temp_convert_input()
