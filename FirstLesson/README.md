<img src="../ignore_toplevelreadme/images/Python.png" width=40>

# CodeHub Python Learn Track

- Downloading Python
- Python's IDLE
- Downloading Visual Studio Code
- How is Python Useful?
- Identifiers & Variables
- Dynamic Typing
- Datatypes
- Integers
- Strings
- Booleans
- Conditionals
- Typecasting
- Input/Output

## Downloading Python

Download Python: https://www.python.org/downloads/

## Python's IDLE

```bash
python3 -m idlelib
```

## Downloading Visual Studio Code

Download VSCode: https://code.visualstudio.com/download

## How is Python Useful?

Python is an Object Oriented Language. Everything in Python is an object! Object-Oriented Programming commonly involves principles such as inheritance, polymorphism, encapsulation and abstraction. Lots of languages use OOP and OOP practices are standard in the Computer Science industry.

Python is also a high level language. All this *really* means is that Python abstracts much of how the computer actually works into something easier to read and write!

```python
for x in range(5):
    print(x)
```

This for-loop prints the numbers 0-4. I am sure that you could at least partially guess what it does.

Additionally, Python uses an interpreter to read and run a Python file. In the terminal, `"python3"` in the command below is calling the interpreter to run the file.

```bash
python3 filename.py
```

## Identifiers & Variables

Python needs to attach a name to an entity. Entities are but not limited to variables, functions and classes. Identifiers can have A-Z, a-z, _, 0-9. However, it cannot start with a number or contain any special characters.

Variables are a special type of identifier. It is assigned a specific value by the author of that variable.

```python
a = 5
```

Here, the variable is `a`.

## Dynamic Typing

Python is dynamically typed, which enables things like the following code to work.

```python
a = 5
a = "I changed a into a String"
```

To understand why this works, imagine pointing at someone in a crowd. Then, point to someone else. That is essentially what `a` is doing. Instead of pointing to an integer object, it now points to a string object.

Since nothing pointst that holds 5, the memory it used can be reclaimed by Python. However, if something points at the same integer object then Python cannot reclaim that memory.

For instance:

```python
a = 5
b = a
a = "I changed a into a String"
```

`b` now points to the exact same object that `a` was pointing to.

## Datatypes

There are many data types in Python.

Integers hold whole numbers and you can do PEMDAS + modulo operations on them. You can also define them in base 10, 16, 8 and 2.

Strings are a collection of characters. For instance, `'a'` is a string containing a single character and `"aaa"` is a string containing three characters. Python does not have a separate character datatype, so even a single character is stored as a string.

## Integers

Integers represent whole numbers. They can be positive, negative or zero.

```python
a = 5
b = -10
c = 0
```

Python allows us to perform arithmetic operations on integers.

```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulo
print(a ** b) # Exponent
```

Python follows the normal order of operations when evaluating mathematical expressions.

```python
a = 5 + 2 * 3

print(a)
```

This will print `11` because multiplication happens before addition.

Modulo `%` returns the remainder after division.

```python
print(10 % 3)
```

This prints `1` because 10 divided by 3 has a remainder of 1.

Integers can also be written in different number systems.

```python
decimal = 10
binary = 0b1010
octal = 0o12
hexadecimal = 0xA
```

All four of these represent the integer `10`.


## Strings

Strings are used to represent text. You can create a string using either single quotes `' '` or double quotes `" "`.

```python
name = "Bob"
message = 'Hello World!'
```

Python does not have a separate datatype for individual characters. A single character is simply a string with a length of 1.

```python
letter = "A"
word = "Apple"
```

You can combine strings together using `+`. This is called concatenation.

```python
firstName = "John"
lastName = "Smith"

fullName = firstName + " " + lastName

print(fullName)
```

This prints:

```text
John Smith
```

You can access individual characters inside a string using an index. Python starts counting indexes at `0`.

```python
word = "Python"

print(word[0])
print(word[1])
```

This prints:

```text
P
y
```

You can also find the length of a string using `len()`.

```python
word = "Python"

print(len(word))
```

This prints `6` because `"Python"` contains 6 characters.


## Booleans

A boolean represents one of two possible values:

```python
True
False
```

Notice that `True` and `False` start with capital letters in Python.

Boolean values are commonly produced by comparisons.

```python
print(5 > 3)
print(5 < 3)
```

This prints:

```text
True
False
```

Python has several comparison operators.

```python
a == b  # Equal to
a != b  # Not equal to
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal to
a <= b  # Less than or equal to
```

Be careful with `=` and `==`.

`=` assigns an object to a variable.

```python
a = 5
```

`==` compares two values.

```python
a == 5
```

Booleans can also be combined using `and`, `or` and `not`.

```python
age = 20
hasTicket = True

print(age >= 18 and hasTicket)
```

`and` requires both conditions to be true.

`or` requires at least one condition to be true.

`not` reverses a boolean value.

```python
print(not True)
```

This prints:

```text
False
```


## Conditionals

Conditionals allow our program to make decisions.

An `if` statement runs code only when its condition is `True`.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Python uses indentation to determine what code belongs inside the `if` statement.

```python
age = 20

if age >= 18:
    print("This is inside the if statement")

print("This is outside the if statement")
```

We can use `else` when we want something different to happen if the condition is `False`.

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

We can use `elif` when we want to check another condition.

```python
temperature = 80

if temperature >= 90:
    print("It is hot!")
elif temperature >= 70:
    print("It is nice outside!")
else:
    print("It is cold!")
```

Python checks these conditions from top to bottom. Once it finds a condition that is `True`, it runs that section and skips the rest.


## Typecasting

Sometimes we need to convert an object from one datatype into another datatype. This is called typecasting.

For example:

```python
number = "5"
```

Even though `"5"` looks like a number, it is actually a string because it is inside quotation marks.

We can convert it into an integer using `int()`.

```python
number = "5"

number = int(number)

print(number + 5)
```

This prints:

```text
10
```

Some common type conversions are:

```python
int("5")
float("5.5")
str(5)
bool(1)
```

You cannot always convert one datatype into another.

For example:

```python
number = int("Hello")
```

Python cannot turn `"Hello"` into an integer, so this will cause an error.


## Input/Output

Programs become much more useful when they can communicate with the user.

We have already been using `print()` to output information.

```python
print("Hello World!")
```

We can get information from the user using `input()`.

```python
name = input("What is your name? ")

print("Hello " + name)
```

The program will wait for the user to type something and press Enter.

One very important thing to remember is that `input()` returns a string.

For example:

```python
age = input("How old are you? ")
```

Even if the user enters:

```text
20
```

`age` contains the string `"20"`, not the integer `20`.

This means the following will not work:

```python
age = input("How old are you? ")

print(age + 5)
```

We can use typecasting to convert the input into an integer.

```python
age = input("How old are you? ")
age = int(age)

print(age + 5)
```

We can also do both on the same line.

```python
age = int(input("How old are you? "))
```

Now we can combine input, typecasting, booleans and conditionals together.

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")
else:
    print("You are not an adult!")
```

This combines many of the concepts we have learned so far into one program!