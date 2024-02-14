"""Print even length words in a string. 

Sample String : ''I love coding" 

Expected Result : “love, coding” """

def even_length_words(string):
    words = string.split()
    even = [x for x in words if len(x) % 2 == 0]
    result = ", ".join(even)
    print("Even length words in given string :", result)

string = input("Enter a string :")
even_length_words(string)
