# -*- coding: UTF-8 -*-
filename = 'guestbook.txt'

while True:
    message = input("What do you like about programming (type 'q' to quit): ")
    if  message != 'q':
        entry = (message + "\n")
        with open(filename, 'a') as file_object:
            file_object.write(entry)
    else:
        break



