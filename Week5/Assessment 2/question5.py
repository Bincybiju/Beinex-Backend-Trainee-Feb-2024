"""Implement a program that reads a text file and counts the occurrences of 
each word, ignoring case sensitivity."""

from collections import Counter


def count_words(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().lower().split()
            word_counts = Counter(words)

        for word, count in word_counts.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


filename = input("Enter the filename: ")
count_words(filename)
