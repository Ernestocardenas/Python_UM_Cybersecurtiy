#This app will take user input and run until the final number is 1 using the collatz conjecture

def main():


    # define variables
    # this collects user input
    X = int(input("pick any positive number: "))
    numCalc = int(1)
    numNot1 = True

    while numNot1:
        if X > 1:
            if (X % 2) == 0:
                X = int(X / 2)
                numCalc += 1
            else:
                X = int(3 * X + 1)
                numCalc += 1
        else:
            # Used for debug print("Your number is",X)
            numNot1 = False

    print("Your number has reached {0}".format(X))
    print("It took {0} calculations to complete".format(numCalc))

    restart=input("Type yes if you would like to start again: ").lower()
    if restart == "yes":
        main()
    else:
        exit()
main()