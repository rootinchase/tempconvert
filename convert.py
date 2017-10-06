# convert.py
# A program to convert tempratures
# by: Ryan Chase

def main():
    print("This program to convert Celsius tempratures to Fahrenheit")
    for x in range (5):
        #this gets the user specified temprature
        temp_first = eval(input("What is the first temperature? "))
        #we now need to know what conversion they want
        print("What unit of temprature is this?")
        unit = input('Enter "C" for Celsius, or "F" for Fahrenheit')
        if unit == "C":
                    temp_second = convert_celsius(temp_first)
                    print("The temperature is", temp_second, "degrees Fahrenheit.")
                    
        elif unit == "F":
            #This is how it calls upon the conversion function for Fahrenheit
            temp_second = convert_fahrenheit(temp_first)
            #This outputs the converted user specified temprature
            print("The temperature is", temp_second, "degrees Celsius.")
                    
        else:
            print("Unsupported input, please try again.")
            x = x-1

def convert_celsius(temp_first):
    #This function converts celsius to fahrenheit
    temp_second = 9/5 * temp_first + 32
    return temp_second
    
def convert_fahrenheit(temp_first):
    #This function converts fahrenheit to celcius (not used yet)
    temp_second = (temp_first - 32) * 5/9
    return temp_second
    

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
