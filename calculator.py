import os


print("--WELCOME TO MY CALCULATOR--")
print("[1] ADDITION")
print("[2] SUBTRACT")
print("[3] DIVIDE")
print("[4] MULTIPLY")
print("[5] REMAINDER")
print("[6] POWER")
print('[7] EXIT')


user_operator = input("Enter your choice: ")
while user_operator in ['1', '2', '3', '4', '5', '6'] and user_operator != '7':
    os.system('cls')
    try:
        num1 = float(input("[?] Enter 1st number: "))
        num2 = float(input("[?] Enter 2nd number: "))
        if user_operator == '1':
            print(f"{num1} + {num2} = ", num1 + num2)
        elif user_operator == '2':
            print(f"{num1} - {num2} = ", num1 - num2)
        elif user_operator == '3':
            if num2 == 0:
                print("Could not divide by zero.")
                break
            print(f"{num1} / {num2} = ", num1 / num2)
        elif user_operator == '4':
            print(f"{num1} * {num2} = ", num1 * num2)
        elif user_operator == '5':
            print(f"{num1} % {num2} = ", num1 % num2)
        else:
            print(f"{num1} ** {num2} = ", num1 ** num2)
        break
    except ValueError:
        print("INVALID, ENTER A NUMBER NOT A STRING!")