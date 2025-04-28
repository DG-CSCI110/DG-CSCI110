#-------------------------------------------------------------------------------
# Name:        Chapter 13
# Purpose:     Section 13.11 Problem 1
#
# Author:      DylanG
#
# Created:     04/27/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

f = open("Songs.txt", "rb")
s = f.readlines()
f.close()
f = open("Newsongs.txt", "wb")
s.reverse()
for line in s:
    f.write(line)
f.close()


