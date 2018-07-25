from name_function import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease type a first name: ")
    if first == 'q':
        break
    last = input("\nType a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("look how pretty I made it: " + formatted_name)
