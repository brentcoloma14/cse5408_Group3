# Isai Ramirez-Lopez, Brent Coloma, Justin Frias
# Group 3: Smart Watering System
# CSE 5408, Spring 2022
# Lab 3: Version Control System GitHub-advanced


# Question 1
def reverse_string():
    user_string = input("Input a string: ")     #user input a string
    print(user_string[::-1])                    #the string is reversed then printed
    print("\n")

reverse_string()

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

#Question 3
def military_time():
    t = input("Input time (Format: 00:00AM): ")     #user input time
    if t[-2:] == "AM":
        if t[:2] == "12":
            time = str("00" + t[2:8])           #If input time is "AM" and the number is 12,
        else:                                   #12 is changed to "00" and the rest of time is continued on
            time = t[:-2]
    else:
        if t[:2] == "12":
            time = t[:-2]
        else:
            time = str(int(t[:2]) + 12) + t[2:8]
    print (time)

military_time()