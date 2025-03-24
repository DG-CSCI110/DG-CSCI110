#-------------------------------------------------------------------------------
# Name:        Chapter 5
# Purpose:     Section 5.14 Problem 1
#
# Author:      DylanG
#
# Created:     03/23/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

def days_of_week(day):
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5: 
        print("Friday")
    elif day == 6: 
        print("Saturday")
    else:
        print("Invalid Input")

day_number = int(input("Enter a number between 1 and 7: "))

days_of_week(day_number)