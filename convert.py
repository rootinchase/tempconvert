# convert.py
# A program to convert tempratures
# by: Ryan Chase

def main():
    print("This program to convert tempratures betweeen units")
    for x in range (5):
        #this gets the user specified temprature
        temp_first = eval(input("What is the first temperature? "))
        #we now need to know what conversion they want
        print("What unit of temprature is this in?")
        unit_current = input('Enter "C" for Celsius, or "F" for Fahrenheit: ')
        #This is to select the final unitfinal unit selection
        print("What do you want this in? ")
        unit_final = input('Enter "C" for Celsius, or "F" for Fahrenheit: ')
        if (unit_current == "C" or unit_current == "c") and (unit_final == "F" or unit_final == "f"):
            #This is how it converts Celsius to Fahrenheit
            temp_second = convert_celsius(temp_first)
            print("The temperature is", temp_second, "degrees Fahrenheit.")
                    
        elif (unit_current == "F" or unit_current == "f") and (unit_final == "C" or unit_final == "c"):
            Celsius
            temp_second = convert_fahrenheit(temp_first)
            #This outputs the converted user specified temprature
            print("The temperature is", temp_second, "degrees Celsius.")

        elif (unit_current == "F" or unit_current == "f") and (unit_final == "k" or unit_final == "K"):
            #This is how it converts Fahrenheit to Kelvin
            #First It converts Fahrenheit to Celsius
            temp_second = convert_fahrenheit(temp_first)
            #Then in converts Celsius to Kelvin
            temp_final = convert_kelvin(temp_second)
            print("The temperature is", temp_final, "degrees Kelvin")

        elif (unit_current == "C" or unit_current == "c") and (unit_final == "k" or unit_final == "K"):
            #This is how it converts Celsuis to Kelvin
            temp_second = convert_kelvin(temp_first)
            print("The temperature is", temp_second, "degrees Kelvin")
                   
        else:
            print("Unsupported input, please try again.")
            x = x-1

def convert_celsius(temp_input):
    #This function converts celsius to fahrenheit
    temp_output = 9/5 * temp_input + 32
    return temp_output
    
def convert_fahrenheit(temp_input):
    #This function converts fahrenheit to celcius (not used yet)
    temp_output = (temp_input - 32) * 5/9
    return temp_output

def convert_kelvin(temp_input):
    #This function converts celsius to kelvin
    temp_output = temp - 273.15
    return temp_output

def table():
    #this creates a table of celcius - fahrenheit conversions
    #an explanation
    print("This is a simple table of Celcius - Fahrenheit conversions")
    #this does 0-100 by 10's, that is 11 numbers, so 11 loops
    for x in range (11):
        #the index gets multiplied by 10 befofe it gets conveted
        temp_first = convert_celsius(10*x)
        print(10*x,"    ",temp_second)
    #The "input()" prevents the program from closing after everything
    #finishes until the press enter
    input()

    
#it's useless to have functions, and not call on them...         
main()
table()
