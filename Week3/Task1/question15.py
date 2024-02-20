""" Write a Python program to check if a string is an anagram of another string.("listen", "silent")
"""



str1 = input("Enter first string :")
str2 = input("Enter second string :")

sorted_str1 = sorted(list(str1.lower()))
sorted_str2 = sorted(list(str2.lower()))

if sorted_str1 == sorted_str2:
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")