# -*- coding: UTF-8 -*-
filename = 'guestbook.txt'

while True:
    name = input("What is your name?: ")
    message = input("Type a short message for the other guest \(type 'q' to quit\): ")
    if name != 'q' or message != 'q':
        entry = (name + "\n" + message + "\n\n")
        with open(filename, 'a') as file_object:
            file_object.write(entry)
    else:
        break



