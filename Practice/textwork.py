filename = input("Type the name of the file: ")
word = input("What word shall we count? ")
number=0
try:
    with open(filename, encoding='UTF-8') as f_obj:
        for line in f_obj.readlines():
            number += line.lower().count(word)
except FileNotFoundError:
    print("No such file")
else:
    print(number)

