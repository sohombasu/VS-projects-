y = int(input("Enter the year:"))

if (y%400 == 0) and (y%100 == 0):
    print("The following year is a leap year",y)

if (y%4  == 0) and (y%100 != 0):
    print("The following year is a leap year",y)

else:
    print("The following year is not a leap year",y)

