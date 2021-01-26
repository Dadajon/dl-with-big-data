# -*- coding: utf-8 -*-
"""
Spyder Editor

Date: 2021/01/14

"""

#%%
"""
Python Comparison Operators
Comparison operators are used to compare two values:

==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
(4 < 5) and (5 < 6)
(1 == 2) or (1 == 1)

#%%
"""
Python Logical Operators
Logical operators are used to combine conditional statements

and -> Returns True if both statements are true -> x < 5 and  x < 10	
or -> Returns True if one of the statements is true -> x < 5 or x < 4	
not ->	Reverse the result, returns False if the result is true -> not(x < 5 and x < 10)
"""

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


# Returns True if both statements are true
True and True
True and False
False and True
False and False

# Returns True if one of the statements is true
True or True
True or False
False or True
False or False

# Reverse the result, returns False if the result is true
not True
not False
not not not not True

#%%
"""
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

is -> Returns True if both variables are the same object -> x is y	
is not -> Returns True if both variables are not the same object -> x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y



#%%
"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:
    
in -> Returns True if a sequence with the specified value is present in the object -> x in y	
not in -> Returns True if a sequence with the specified value is not present in the object -> x not in y
"""
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list


#%%

name = "Mary"
password = "swordfish"
if name == "Mary":
    print("Hello, Mary")
    if password == "swordfish":
        print("Access granted")
    else:
        print("Wrong password")

#%%
"""
Python Conditions and If statements

The most common type of flow control statement is the if statement. An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

In plain English, an if statement could be read as, “If this condition is true, execute the code in the clause.” In Python, an if statement consists of the following:

The if keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the if clause)
"""

a = 33
b = 200
if b > a:
    print("b is greater than a")
    
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
    
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

"""
Bonus

Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
"""
# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


"""
Combined conditional statements

AND
The and keyword is a logical operator, and is used to combine conditional statements

OR
The or keyword is a logical operator, and is used to combine conditional statements
"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
    
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

#%%
"""
while Loop Statements

You can make a block of code execute over and over again using a while statement. The code in a while clause will be executed as long as the while statement’s condition is True. In code, a while statement always consists of the following:

The while keyword
A condition (that is, an expression that evaluates to True or False)
A colon
Starting on the next line, an indented block of code (called the while clause)
"""

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
    print('Thank you!')

#%%
"""
for Loops and the range() Function

The while loop keeps looping while its condition is True (which is the reason for its name), but what if you want to execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and includes the following:

The for keyword
A variable name
The in keyword
A call to the range() method with up to three integers passed to it
A colon
Starting on the next line, an indented block of code (called the for clause)
"""

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

#%%
"""
As another for loop example, consider this story about the mathematician Carl Friedrich Gauss. When Gauss was a boy, a teacher wanted to give the class some busywork. The teacher told them to add up all the numbers from 0 to 100. Young Gauss came up with a clever trick to figure out the answer in a few seconds, but you can write a Python program with a for loop to do this calculation for you.

The result should be 5,050.
"""

total = 0
for num in range(101):
    total = total + num
print(total) 

#%%
"""
The Starting, Stopping, and Stepping Arguments to range()

Some functions can be called with multiple arguments separated by a comma, and range() is one of them. This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.
"""

# The first argument will be where the for loop’s variable starts, and the second argument will be up to, but not including, the number to stop at
for i in range(12, 16):
    print(i)
    
# The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
for i in range(0, 10, 2):
    print(i)

# The range() function is flexible in the sequence of numbers it produces for for loops. For example (I never apologize for my puns), you can even use a negative number for the step argument to make the for loop count down instead of up.
for i in range(5, -1, -1):
    print(i)

#%%
"""
Importing Modules

All Python programs can call a basic set of functions called built-in functions, including the print(), input(), and len() functions you’ve seen before. Python also comes with a set of modules called the standard library. Each module is a Python program that contains a related group of functions that can be embedded in your programs. For example, the math module has mathematics-related functions, the random module has random number-related functions, and so on.

Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

- The import keyword
- The name of the module
- Optionally, more module names, as long as they are separated by commas

Once you import a module, you can use all the cool functions of that module. Let’s give it a try with the random module, which will give us access to the random.randint() function.
"""

import random
for i in range(5):
    print(random.randint(1, 10))


# An import statement that imports four different modules
import random, sys, os, math

#%%
"""
from import Statements

An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.

With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the import random form of the statement.
"""
# math.pow(x, y)
# Return x raised to the power y
from math import pow

x=2
y=3
print(pow(x,y))


# math.sqrt(x)
# Return the square root of x.
from math import sqrt

x=81
print(sqrt(x))

#%%
"""
A Short Program: Guess the Number
    set a random number between 1 and 20 and guess it!

Example:
    print "I am thinking of a number between 1 and 20."
    print "Take a guess.""
    input 10
    print "Your guess is too low."
    print "Take a guess."
    input 15
    print "Your guess is too low."
    print "Take a guess."
    input 17
    print "Your guess is too high."
    print "Take a guess."
    input 16
    print "Good job! You guessed my number in 4 guesses!"
"""

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


#%%
"""
A Short Program: Rock, Paper, Scissors

Example:
    ROCK, PAPER, SCISSORS
    0 Wins, 0 Losses, 0 Ties
    Enter your move: (r)ock (p)aper (s)cissors or (q)uit
    p
    PAPER versus...
    PAPER
    It is a tie!
    0 Wins, 1 Losses, 1 Ties
    Enter your move: (r)ock (p)aper (s)cissors or (q)uit
    s
    SCISSORS versus...
    PAPER
    You win!
    1 Wins, 1 Losses, 1 Ties
    Enter your move: (r)ock (p)aper (s)cissors or (q)uit
    q
"""

import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1


