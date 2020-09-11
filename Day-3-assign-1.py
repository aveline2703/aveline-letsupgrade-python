altitude = int(input("Enter Altitude in ft:"))
if altitude<=1000:
    print("Safe to land")
elif altitude< 5000:
    print("Bring down to 1000")
else:
    print("Turn Around and Try Again")