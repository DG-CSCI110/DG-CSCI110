#-------------------------------------------------------------------------------
# Name:        Chapter 20
# Purpose:     Section 20.8 Problem 3
#
# Author:      DylanG
#
# Created:     04/27/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
import string

def alice_word(word, word_counts):
    word = word.lower().strip(string.punctuation)
    if word:
        word_counts[word] = word_counts.get(word,0) + 1

def write_word_counts(word_counts, filename):
    with open(filename, "w") as file:

        file.write("Word          Count\n")
        file.write("===================\n")

        for word, count in sorted(word_counts.items()):
            file.write(f"{word:<18} {count}\n")

def main():
    word_counts = {}

    with open("alice.txt","r") as file:
        for line in file:
            words = line.split()
            for word in words:
                alice_word(word, word_counts)

    alice_count = word_counts.get("alice", 0)
    print(f"How Many Times Does The Word 'Alice' Occur In The Book? {alice_count}")

    write_word_counts(word_counts, "alice_words.txt")


if __name__ == '__main__':
    main()