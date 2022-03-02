# Isai Ramirez-Lopez, Brent Coloma, Justin Frias
# Group 3: Smart Watering System
# CSE 5408, Spring 2022
# Lab 3: Version Control System GitHub-advanced


#Question 2
def prime():
    x = int(input("Input a number: "))      #user inputs an integer
    for i in range(2, x):
        if (x % i == 0):                    #the user input is divided by the i which increments
            print ("Number is not prime.")  #until i is equal to user input. If the remainder is 0, the number
            print("\n")
            i = i + 1                       #is not prime.
            break
    else:
        print ("Number is prime.")          #if for loop processes without a remainder 0, then the number is prime.
        print("\n")

prime()
