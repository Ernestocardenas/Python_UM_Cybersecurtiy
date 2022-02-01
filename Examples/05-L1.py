# Define a function that receives two numbers and
# an operator and performs the calculation inside the function, and returns the solution.

from Examples.time_functions import monthyear



def calculator(number1, number2, operator):
    try:
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "/":
            result = number1 / number2
        elif operator == "*":
            result = number1 * number2
        else:
            result = "INCORRECT INPUT ENTERED"
    except:
        print("Syntax Error, please try again!")

    return result

usernumber1 = int(input("Please enter your first number: "))
usernumber2 = int(input("Please enter your second number: "))
useroperator = input("Please enter your operation (+,-,/,*)")

userresult = calculator(usernumber1, usernumber2, useroperator)

print(userresult)
print(monthyear())