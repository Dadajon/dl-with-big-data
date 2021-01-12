operator = input("Operator (+, -, *, /): ")
num1 = input("First Number: ")
num2 = input("Second Number: ")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out = num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2

print("Answer: " + str(out))
