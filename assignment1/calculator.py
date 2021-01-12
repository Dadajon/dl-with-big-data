# TODO 1: Enter two numbers that you want to compute.
# TODO 2: Add a mathematical operator: + for addition.
# TODO 3: Print some more context to fully inform the user throughout the runtime of the program
# TODO 4: Add the rest of the operators to the program with the same format you have used for addition.
# TODO 5: Add conditional statements into the program.
# TODO 6: Save python file as calculator.py


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
