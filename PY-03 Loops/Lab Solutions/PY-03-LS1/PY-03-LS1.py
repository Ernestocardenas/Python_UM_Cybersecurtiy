"""Lab Objective: Understand how to work with loops and the range function in a script."""


upper_bound = int(input("Choose the range upper bound --> "))

for x in range(1, upper_bound):
    print("The next number in line is {}".format(x))

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
