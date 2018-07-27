filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Skriv in ditt födelsedatum i formatet ÅÅMMDD:')
if birthday in pi_string:
    print('Ditt födelsedatum finns i de första miljoner decimalerna i pi!')
else:
    print('Ditt födelsedatum finns inte i de första miljoner decimalerna i pi :(')
