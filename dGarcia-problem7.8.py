#-------------------------------------------------------------------------------
# Name:        Chapter 7
# Purpose:     Section 7.26 Problem 9
#
# Author:      DylanG
#
# Created:     03/30/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

def newtonSqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    while better !=approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        print("Approx:", better)
    return approx



print("Final approx:", newtonSqrt(25))