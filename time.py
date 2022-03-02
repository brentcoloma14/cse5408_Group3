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