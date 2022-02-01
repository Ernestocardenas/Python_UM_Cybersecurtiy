import time

num = input('Please provide a number to prove Collatz Conjecture: ')

absNum = abs(int(num))

solved = False

while solved != True:
    if absNum % 2 == 0:
        absNum /= 2
        print(str(absNum))
    elif absNum % 2 == 1:
        absNum = absNum * 3 + 1
        print(str(absNum))
    else:
        solved = True