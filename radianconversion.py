#!/usr/bin/env python3

#The following code is used to
#convert radians to degrees and
#degrees into radians.


#Import cmath library
import cmath

#converts radians into  degrees
def radcon():
    while True:
        try:
            x = float(input("Enter Radian: "))

        except ValueError:
                print("Invalid entry. Please try again")
                
        else:
            p = cmath.pi
            d = float((180 * x)/p)
            print("the provided radian converts to: ", d , "degrees")
            break
        

#converts degrees into radians
def degcon():
    while True:
        try:
            y = float(input("Enter Degrees: "))

        except ValueError:
                print("Invalid entry. Please try again")
        else:
            p = cmath.pi
            d = float(y*(p/180))
            print("the provided degrees converts to: ", d , "radians")
            break
        
#select the conversion
def select():
    z = input()
    if  z == "1":
        radcon()
    elif z == "2":
        degcon()
    else:
        print("Invalid selection. Please try again")



print("what do you want to convert?")
print("1. I want to convert radians to degrees.")
print("2. I want to convert degrees to radians.")
print("Enter option 1 or 2: ")

select()
    
        








    

        
