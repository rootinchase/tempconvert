# convert_terminal.py
# A program to convert temperatures
# by: Ryan Chase


def main():
    print("This program to convert temperatures between units")
    for x in range(5):
        # this gets the user specified temperature
        temp = eval(input("What is the first temperature? "))
        # we now need to know what conversion they want
        print("What unit of temperature is this in? ")
        print('Enter "C" for Celsius, or "F" for Fahrenheit,')
        unit_current = input('or "K" for Kelvin, or "R" for Rankine: ')
        # This is to select the final unit
        print('Using the same abbreviations as before,')
        unit_final = input("What do you want this in? ")
        unit_current = unit_current[0].upper()
        unit_final = unit_final[0].upper()

        if (unit_current == "C") and (unit_final == "F"):
            # This is how it converts Celsius to Fahrenheit
            temp = convert_celsius_f(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Fahrenheit.")
                    
        elif (unit_current == "F") and (unit_final == "C"):
            # Convert Fahrenheit to Celsius
            temp = convert_fahrenheit_c(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Celsius.")

        elif(unit_current == "R") and (unit_final == "F"):
            # This is how it converts Fahrenheit to Kelvin
            # It converts Rankine to Fahrenheit
            temp = convert_rankine_f(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Kelvin")

        elif (unit_current == "R") and (unit_final == "C"):
            # This is how it converts Fahrenheit to Kelvin
            # First It converts Rankine to Fahrenheit
            temp = convert_rankine_f(temp)
            # First It converts Fahrenheit to Celsius
            temp = convert_fahrenheit_c(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Kelvin")

        elif (unit_current == "R") and (unit_final == "K"):
            # This is how it converts Fahrenheit to Kelvin
            # First It converts Rankine to Fahrenheit
            temp = convert_rankine_f(temp)
            # First It converts Fahrenheit to Celsius
            temp = convert_fahrenheit_c(temp)
            # Then in converts Celsius to Kelvin
            temp = convert_celsius_k(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Kelvin")

        elif (unit_current == "F") and (unit_final == "K"):
            # This is how it converts Fahrenheit to Kelvin
            # First It converts Fahrenheit to Celsius
            temp = convert_fahrenheit_c(temp)
            # Then in converts Celsius to Kelvin
            temp = convert_celsius_k(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Kelvin")

        elif (unit_current == "C") and (unit_final == "K"):
            # This is how it converts Celsius to Kelvin
            temp = convert_celsius_k(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Kelvin")

        elif (unit_current == "K") and (unit_final == "F"):
            # This is how it converts Kelvin to Fahrenheit
            # First It converts Kelvin to Celsius
            temp = convert_kelvin_c(temp)
            # Then in converts Celsius to Fahrenheit
            temp = convert_celsius_f(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Fahrenheit.")
            
        elif (unit_current == "K") and (unit_final == "R"):
            # This is how it converts Kelvin to Rankine
            # First It converts Kelvin to Celsius
            temp = convert_kelvin_c(temp)
            # Then in converts Celsius to Fahrenheit
            temp = convert_celsius_f(temp)
            # Finally it converts Fahrenheit to Rankine
            temp = convert_fahrenheit_r(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Rankine.")

        elif (unit_current == "C") and (unit_final == "R"):
            # This is how it converts Celsius to Rankine
            # First It converts Celsius to Fahrenheit
            temp = convert_celsius_f(temp)
            # Finally it converts Fahrenheit to Rankine
            temp = convert_fahrenheit_r(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Rankine.")

        elif (unit_current == "F") and (unit_final == "R"):
            # This is how it converts Celsius to Rankine
            # It converts Fahrenheit to Rankine
            temp = convert_fahrenheit_r(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Rankine.")
            
        elif (unit_current == "K") and (unit_final == "C"):
            # This is how it converts Kelvin to Celsius
            temp = convert_kelvin_c(temp)
            # This outputs the converted user specified temperature
            print("The temperature is", temp, "degrees Celsius")

        else:
            print("Unsupported input, please try again.")


def convert_fahrenheit_c(imputed):
    # This function converts fahrenheit to celcius
    temp_output = (imputed - 32) * 5/9
    return temp_output


def convert_celsius_f(imputed):
    # This function converts celsius to fahrenheit
    temp_output = 9/5 * imputed + 32
    return temp_output


def convert_celsius_k(imputed):
    # This function converts celsius to kelvin
    output = imputed + 273.15
    return output


def convert_kelvin_c(imputed):
    # This function converts kelvin to celsius
    output = imputed - 273.15
    return output


def convert_rankine_f(imputed):
    # This function converts Rankine to Fahrenheit
    output = imputed + 459.67
    return output


def convert_fahrenheit_r(imputed):
    # This function converts fahrenheit to Rankine
    temp_output = imputed - 459.67
    return temp_output


# it's useless to have functions, and not call on them...
main()

