#-------------------------------------------------------------------------------
# Name:        Chapter 19
# Purpose:     Section 19.6 Problem 1
#
# Author:      DylanG
#
# Created:     05/16/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import simpledialog

def readposint():
    root = tk.Tk()
    root.withdraw()

    while True:
        user_input = simpledialog.askstring("Input", "Enter Positive Integer:")


        if user_input is None:
            print("Input Cancelled By User.")
            return None


        if user_input.strip() == "":
            print("No Input Entered. Enter Positive Integer.")
            continue

        try:

            value = int(user_input)


            if value > 0:
                return value
            else:
                print("Enter Positive Integer.")

        except ValueError:

            print("Input Invalid. Enter Positive Integer.")


if __name__ == "__main__":
    positive_integer = readposint()
    if positive_integer is not None:
        print(f"You entered: {positive_integer}")