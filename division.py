print("Type two numbers to be divided")
print("Type 'q' to quit")

while True:
    num1 = input("first number:")
    if num1 == 'q':
        break
    num2 = input("second number")
    if num2 == 'q':
        break
    try:
        answer = (int(num1) / int(num2))
    except ZeroDivisionError:
        print("You can not divide by 0")
    else:
        print(answer)


