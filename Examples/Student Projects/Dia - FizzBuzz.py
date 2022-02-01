# FizzBuzz Job Interview!
# Dia Hughes
# UM Cyber Bootcamp Student April 2021

#Set numbers for fizz and buzz

fizz = 3
buzz = 5

#Set range to count through

First = 1
Last = 100

for i in range(First, Last+1, 1):

    if i % fizz == 0 and i % buzz == 0:
        print("fizzbuzz")

    elif i % fizz == 0:
        print("fizz")

    elif i % buzz == 0:
        print("buzz")

    else:
        print(i)
