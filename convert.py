# convert.py
# A program to convert temperatures
# by: Ryan Chase


def main():
    print("This program to convert temperatures between units")
    for x in range(5):
        # this gets the user specified temperature
        temp_first = eval(input("What is the first temperature? "))
        # we now need to know what conversion they want
        print("What unit of temperature is this in? ")
        print('Enter "C" for Celsius, or "F" for Fahrenheit,')
        unit_current = input('or "K" for Kelvin: ')
        # This is to select the final unit
        print('Using the same abbreviations as before,')
        unit_final = input("What do you want this in? ")
        unit_current = unit_current[0].upper()
        unit_final = unit_final[0].upper()
        if (unit_current == "C") and (unit_final == "F"):
            # This is how it converts Celsius to Fahrenheit
            temp_second = convert_celsius_f(temp_first)
            print("The temperature is", temp_second, "degrees Fahrenheit.")
                    
        elif (unit_current == "F") and (unit_final == "C"):
            # Celsius
            temp_second = convert_fahrenheit_c(temp_first)
            # This outputs the converted user specified temperature
            print("The temperature is", temp_second, "degrees Celsius.")

        elif (unit_current == "F") and (unit_final == "K"):
            # This is how it converts Fahrenheit to Kelvin
            # First It converts Fahrenheit to Celsius
            temp_second = convert_fahrenheit_c(temp_first)
            # Then in converts Celsius to Kelvin
            temp_final = convert_celsius_k(temp_second)
            print("The temperature is", temp_final, "degrees Kelvin")

        elif (unit_current == "C") and (unit_final == "K"):
            # This is how it converts Celsius to Kelvin
            temp_second = convert_celsius_k(temp_first)
            print("The temperature is", temp_second, "degrees Kelvin")

        elif (unit_current == "K") and (unit_final == "F"):
            # This is how it converts Kelvin to Fahrenheit
            # First It converts Kelvin to Celsius
            temp_second = convert_kelvin_c(temp_first)
            # Then in converts Celsius to Fahrenheit
            temp_final = convert_celsius_f(temp_second)
            print("The temperature is", temp_final, "degrees Fahrenheit.")
            
        elif (unit_current == "K") and (unit_final == "C"):
            # This is how it converts Kelvin to Celsius
            temp_second = convert_kelvin_c(temp_first)
            print("The temperature is", temp_second, "degrees Celsius")

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
