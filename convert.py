# convert.py
# A program to convert tempratures
# by: Ryan Chase

def main():
    print("This program to convert tempratures betweeen units")
    for x in range (5):
        #this gets the user specified temprature
        temp_first = eval(input("What is the first temperature? "))
        #we now need to know what conversion they want
        print("What unit of temprature is this in? ")
        print('Enter "C" for Celsius, or "F" for Fahrenheit,')
        unit_current = input('or "K" for Kelvin: ')
        #This is to select the final unit
        print('Using the same abbreveations as before,')
        unit_final = input("What do you want this in? ")
        if (unit_current == "C" or unit_current == "c") and (unit_final == "F" or unit_final == "f"):
            #This is how it converts Celsius to Fahrenheit
            temp_second = convert_celsius_f(temp_first)
            print("The temperature is", temp_second, "degrees Fahrenheit.")
                    
        elif (unit_current == "F" or unit_current == "f") and (unit_final == "C" or unit_final == "c"):
            Celsius
            temp_second = convert_fahrenheit_c(temp_first)
            #This outputs the converted user specified temprature
            print("The temperature is", temp_second, "degrees Celsius.")

        elif (unit_current == "F" or unit_current == "f") and (unit_final == "k" or unit_final == "K"):
            #This is how it converts Fahrenheit to Kelvin
            #First It converts Fahrenheit to Celsius
            temp_second = convert_fahrenheit_c(temp_first)
            #Then in converts Celsius to Kelvin
            temp_final = convert_celsius_k(temp_second)
            print("The temperature is", temp_final, "degrees Kelvin")

        elif (unit_current == "C" or unit_current == "c") and (unit_final == "k" or unit_final == "K"):
            #This is how it converts Celsuis to Kelvin
            temp_second = convert_celsius_k(temp_first)
            print("The temperature is", temp_second, "degrees Kelvin")

        elif (unit_current == "K" or unit_current == "k") and (unit_final == "F" or unit_final == "f"):
            #This is how it converts Kelvin to Fahrenheit
            #First It converts Kelvin to Celsius
            temp_second = convert_kelvin_c(temp_first)
            #Then in converts Celsius to Fahrenheit
            temp_final = convert_celsius_f(temp_second)
            print("The temperature is", temp_final, "degrees Fahrenheit.")

        elif (unit_current == "K" or unit_current == "k") and (unit_final == "C" or unit_final == "c"):
            #This is how it converts Kelvin to Celsuis
            temp_second = convert_kelvin_c(temp_first)
            print("The temperature is", temp_second, "degrees Celsius")       
                   
        else:
            print("Unsupported input, please try again.")
            x = x-1
    
def convert_fahrenheit_c(temp_input):
    #This function converts fahrenheit to celcius
    temp_output = (temp_input - 32) * 5/9
    return temp_output

def convert_celsius_f(temp_input):
    #This function converts celsius to fahrenheit
    temp_output = 9/5 * temp_input + 32
    return temp_output

def convert_celsius_k(temp_input):
    #This function converts celsius to kelvin
    temp_output = temp_input + 273.15
    return temp_output

def convert_kelvin_c(temp_input):
    #This function converts kelvin to celsius
    temp_output = temp_input - 273.15
    return temp_output

def convert_rankine_f(temp intro):
    #This function converts Rankine to Fahrenheit
    temp_output = temp_input + 459.67
    return temp_output

def convert_fahrenheit_R
    #This function converts fahrenheit to Rankine
    temp_output = temp_input - 459.67
    return temp_output

def table():
    #this creates a table of celcius - fahrenheit conversions
    #an explanation
    print("This is a simple table of Celcius - Fahrenheit conversions")
    #this does 0-100 by 10's, that is 11 numbers, so 11 loops
    for x in range (11):
        #the index gets multiplied by 10 befofe it gets conveted
        temp_first = convert_celsius_f(10*x)
        print(10*x,"    ",temp_second)
    #The "input()" prevents the program from closing after everything
    #finishes until the press enter
    input()

    
#it's useless to have functions, and not call on them...         
main()
table()
