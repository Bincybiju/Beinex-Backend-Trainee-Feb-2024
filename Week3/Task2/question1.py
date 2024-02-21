""" Write a Python program to read an entire text file. 
"""


try:
    f = open('file1.txt', 'w')
    f.write("Hai Welcome to File handling \nHi guys \nBye \nHello world")
    f.close()

    f = open('file1.txt', 'r')
    print(f.read())
    f.close()
except:
    print("An error occured")



