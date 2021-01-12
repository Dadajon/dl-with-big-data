# Calculator

![Spyder](https://img.shields.io/badge/Spyder-4.0.0-red)
![Python](https://img.shields.io/badge/Python-3.8.5-blue)

1. Enter two numbers that you want to compute.

    **Tips:** To do this, you should use Python's built-in input() function that accepts user-generated input from the keyboard. Pass a string to prompt the user inside of the parentheses of the input() function. Assign the user's input to a variable.

2. Add a mathematical operator: + for addition.
3. Print some more context to fully inform the user throughout the runtime of the program.

    **Tips:** To do this, you can use string formatters to format your text and provide feedback properly.

4. Add the rest of the operators to the program with the same format you have used for addition.

    Tips: - for subtraction, * for multiplication, and / for division.

5. Add conditional statements into the program.

    **Tips:** The if statement will be where the addition is performed. There will be three else-if or elif statements for each of the other operators, and the else statement will be put in place to handle an error if the person did not input an operator symbol.

6. Save python file as calculator.py

To walk through this program, first, it prompts the user to put in an operation symbol. We'll say the user inputs * to multiply. Next, the program asks for two numbers, and the user inputs 58 and 40. At this point, the program shows the equation performed and the product.

### Deadline: 2021.01.19 23:59
---

### Bonus

1. Define function calculate() to handle the program's ability as many times as the user wants.

    **Tips**: Put your existing code block into a function. Name the function calculate() and add a layer of indentation within the function itself. To ensure the program runs, call the function at the bottom of the file.

2. Create a second function, again(), to give the user a choice to continue the calculation or not.

    **Tips**: Use conditional statements. You can put function again() off of calculator() conditional statements, but in this case, you will only have one if, one elif, and one else to handle errors.

3. Add additional operators, as ** for power and % for modulo.
4. Improve the code

    **Tips:** Use exception handling with the try ... except statement.