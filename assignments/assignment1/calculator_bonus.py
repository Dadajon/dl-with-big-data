def calculate():
    operation = input("Operator (+, -, *, /): ")
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    if operation == '+':
        print('{} + {} = {}'.format(num1, num2, num1+num2))
    elif operation == '-':
        print('{} - {} = {}'.format(num1, num2, num1-num2))
    elif operation == '*':
        print('{} * {} = {}'.format(num1, num2, num1*num2))
    elif operation == '/':
        print('{} / {} = {}'.format(num1, num2, num1/num2))
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()


def again():
    calc_again = input(
        """Do you want to calculate again? Please type Y for YES or N for NO. """)

    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you later.')


if __name__ == '__main__':
    calculate()
