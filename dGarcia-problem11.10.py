#-------------------------------------------------------------------------------
# Name:        Chapter 11
# Purpose:     Section 11.22 Problem 10
#
# Author:      DylanG
#
# Created:     04/08/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

def replace(s, old, new):
    return new.join(s.split(old))

def test(actual):
    print("Pass" if actual else "Fail")

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
