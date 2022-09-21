_09/17/22, 1:00p-3:00p_

# Python Basics

[Pycharm Installation Instructions](https://bit.ly/3xsoubP)

`print()` Function: Takes a input parameter and writes it to the console

```python
print("Hello World")
print(5)
print([1, 2, 3, 4, 5])
print("Look\nA\nNew\nLine")
```

Comments

```python
# using a hash is a comment in python!
```

Variables: Ways to store information in memory. You can save information and use it multiple times.

```python
x = 5 # Sets the variable x to the number 5
```

## Data Types

String, number, list, object. Can change types at any time, not enforced types.

## Basic Mathmatical Operations

```python
x = 5
y = 12
z = x + y
print(z)

+ # Addition
- # Subtraction
* # Multiplication
/ # Division

x = 10 // 4 #Integer Division (2)
x = 8 % 5 # Remainder of 8/5 (modulo)(3)
x = 5 ** 2 # Power of 5^2 (25)


x += 7 # Add 7 to x
x -= 2 # Subtract 2 from x
x *= 5 # Multiply x by 5
x /= 2 # Divide x by 2
```

### Concatenated strings

```python
c = "Cat"
d = "Dog"

print(c + d) # prints "CatDog"
```
```python
intro = "There are "
wonders = 7
outro = " of the world!"
print(intro + wonders + outro) # Gives an error message. Cannot concatenate str (not "int") to str

# turn 7 into a string, or use str(7), or do the conversion in the final call str(wonders)
```

## Input

`input()` Function: pauses program and allows you to type in the console. After typing, hit enter

```python
name = input("What is your name?")

print("hello " + name)

age = input("How old are you?")

age_difference = 31 - int(age)

print("Wow Python is " + str(age_difference) + " years older than you!")
```
---
## Activity 1:

```python
# 1. Create a new Python file called activity1.py

# 2. Print out “This is for Activity 1 of the ET050 Bootcamp!”
print("This is for Activity 1 of the ET050 Bootcamp")

# 3. Calculate speed of earth in mph assuming earth is 93 million miles
# from the sun and orbits the sun in 365 days (circumference  = 2*pi*radius)
r = 93000000
pi = 3.14
miles = 2 * pi * r
days = 365
hours = days * 24
mph = miles / hours
print("The speed of the earth is " + str(mph) + "!")

# 4. ask user what year they were born
year_born = input("What year were you born?")
print("You were born in " + year_born)

# 5. Calculate how many years old they are
age = 2022 - int(year_born)
print("You are " + str(age) + " years old")

# 6. Calculate the number of heart beats they have had,
# assuming they average 60 beats per minute
heartbeats = 60 * 525600 * age
print("Wow! Your heart has beat an amazing " + str(heartbeats) + " times so far!")

```

## Relational Expressions
`if` statements use logical tests

![Boolean](/img/boolean.png)

Tests can be combined using logical operators

![Combined](/img/combinedoperators.png)

"Truth tables" for each, used with logical values p and q

![truth table](/img/truthtable.png)

Relational Operators have lower precedence than math (PEMDAS)

Logical Operators have lower precedence than relational operators

## Loops

Getting rid of repetition. Repeating an action results in redundant code.

```python
for variable in range (start, stop) :
  statement
  statement
  ...

# start is inclusive, stop is exclusive
```

if variable is less than the stop, then stop, excute statements, increase the variable's value by 1

```python
for i in range(1, 5):
  print(str(i) + " squared = " + str(i * i))

# 1 squared = 1
# 2 squared = 4
# 3 squared = 9
# 4 squared = 16
```

Loop with step

```python
for i in range(1, 5, 2):
  print(str(i) + " squared = " + str(i * i))

# 1 squared = 1
# 3 squared = 9
```

Loops in Loops
```python
variable = 1

for i in range(10):
    print(str(i) * i)

    for j in range(0, i):
        variable = variable + 1

print(variable)

# 46
```
---
## Activity 2: Box Problem


Static Solution:

```python
height = 7
width = 10

print("=" * 10)
print("=", " " * 8, "=", sep="")
print("=", " " * 8, "=", sep="")
print("=", " " * 8, "=", sep="")
print("=", " " * 8, "=", sep="")
print("=", " " * 8, "=", sep="")
print("=" * 10)

# makes
# ==========
# =        =
# =        =
# =        =
# =        =
# =        =
# ==========
```

Looping, Dynamic Solution:

```python
height = 7
width = 10

print("=" * width)

for i in range(height - 2):
    print("=", " " * (width - 2), "=", sep="")

print("=" * width)

# makes
# ==========
# =        =
# =        =
# =        =
# =        =
# =        =
# ==========
```
---
## Activity 3: If-Else Statements

Write code to output grade letter based on the score input from user.
- Print A if the score is greater than or equal to 98
- Print A- if the score is greater than or equal to 95
- Print B+ if the score is greater than or equal to 93
- Print B if the score is greater than or equal to 90
- Print B- if the score is greater than or equal to 85
- Print C+ if the score is greater than or equal to 80
- Print C if the score is greater than or equal to 75
- Print C- if the score is greater than or equal to 70
- Print D if the score is greater than or equal to 60
- Otherwise, print E

```python
data = input("What is your score?")
score = int(data)

if score >= 98:
    print("A")
elif score >= 95:
    print("A-")
elif score >= 93:
    print("B+")
elif score >= 90:
    print("B")
elif score >= 85:
    print("B-")
elif score >= 80:
    print("C+")
elif score >= 75:
    print("C")
elif score >= 70:
    print("C-")
elif score >= 60:
    print("D")
else:
    print("E")
```
___
## Homework

```
Write code to output these two figures using string multiplication and loops.

+/\/\/\/\/\/\/\/\/\/\+
|                    |
|                    |
|                    |	
|                    |
|                    |
+/\/\/\/\/\/\/\/\/\/\+

+/\/\/\/\+
|        |
|        |	
+/\/\/\/\+
```