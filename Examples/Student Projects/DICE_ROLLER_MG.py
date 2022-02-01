# DICE ROLLER
# Michael Gonzalez
# UM Cyber Bootcamp Student Feb 2021


import random

while True:
    print("Hello Adventurer! Would you like to try your luck on some dice?\n")
    answer = input("Press Y for Yes, Or N for No and walk away in shame!\n") # getting our user input
    number = random.randint(1, 20)

    if answer == "Y" or answer == "y": # evaluating that input on our first condition
        print("Rolling the dice! May fate Smile upon you!\n ")
        print(number)
        print("##############################################")

        if number == 1:
            print("Ouch! Critical fail! Better luck next time adventurer!\n ") # If yes, analyze the number
        if number == 2:
            print("Nearly lost your head there adventurer!\n ")
        if number == 3:
            print("Couple of steps away from a critical failure!\n ")
        if number == 4:
            print("Pretty flimsy hit there adventurer, are you ok?\n ")
        if number == 5:
            print("Quarter of the way to a Critical Success!\n ")
        if number == 6:
            print("Not too shabby adventurer! could've been worse!\n ")
        if number == 7:
            print("The Holy Number! Smash through the heresy!\n ")
        if number == 8:
            print("The infinite symbol! do not lose sight in its gaze!\n ")
        if number == 9:
            print("Mighty blow! well done!\n ")
        if number == 10:
            print("Halfway to the top! now give that troll a solid bonk!\n ")
        if number == 11:
            print("Your mind control will not work here! Be gone!\n ")
        if number == 12:
            print("Let the bonks reign down!\n ")
        if number == 13:
            print("Lucky Thirteen! or is it?\n ")
        if number == 14:
            print("POW! right in the kisser!\n ")
        if number == 15:
            print("An Arrow to the knee! that's the enemies last adventure!\n ")
        if number == 16:
            print("I like em Big, I like em Chunky!\n ")
        if number == 17:
            print("The enemy felt that hit in their soul!\n ")
        if number == 18:
            print("That hit was brutal, and we loved every second of it!\n ")
        if number == 19:
            print("OH SO CLOSE! that was an awesome hit!\n ")
        if number == 20:
            print("The RNG Gods Smile upon you! CRITICAL HIT!\n ")

    elif answer == "N" or answer == "n": # If the first statement is not triggered, check for a no....
        print("Walk away in shame adventurer! no risk taking for you it seems. ")
        break

    else: # Our default condition because users are fucking stupid and can't read directions.
        print("Bad Input please enter Y or N!")


