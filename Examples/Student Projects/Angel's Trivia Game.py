# Blood Pressure Monitor
# Adriel
# UM Cyber Bootcamp Student

import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
score = 0
# First question
# Starting with a try block to manage an error in the input of the question like an integer or a float
try:
    question = int(input(Fore.RED + "What port does Telnet use?: "))
    if question == 23:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is: {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########  ")
    else:
        print("That's not it")
        print("Remember T3lnet!")
        print(f"Your current score is: {score} ")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
# If there is no error the code will continue to the next question
# If an error occurs the WHILE loop will circle back to the question until it meets the criteria
# Once a criteria it's met the Break line will exit out that loop into the next question
    while ValueError == ValueError:
        try:
            question = int(input(Fore.RED + "What port does Telnet use?: "))
            if question == 23:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is: {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########  ")
                break
            else:
                print("That's not it")
                print("Remember T3lnet!")
                print(f"Your current score is: {score} ")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Second question starts here
try:
    question2 = int(input(Fore.GREEN + "What port does Secure Shell use?: "))
    if question2 == 22:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print("Remember SSH=22H")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question2 = int(input(Fore.GREEN + "What port does Secure Shell use?: "))
            if question2 == 22:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print("Remember SSH=22H")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Third question starts here
try:
    question3 = int(input(Fore.YELLOW + "What port does Network Time Protocol use?: "))
    if question3 == 123:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print("Remember that time goes 1..2..3")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question3 = int(input(Fore.YELLOW + "What port does Network Time Protocol use?: "))
            if question3 == 123:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print("Remember that time goes 1..2..3")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Fourth question starts here
try:
    question4 = int(input(Fore.CYAN + "What port does Dynamic Host Configuration Protocol use?: "))
    if question4 == 67:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print("DON'T YOU DARE TO FORGET ABOUT D.O.R.A")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question4 = int(input(Fore.CYAN + "What port does Dynamic Host Configuration Protocol use?: "))
            if question4 == 67:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print("DON'T YOU DARE TO FORGET ABOUT D.O.R.A")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Fifth question starts here
try:
    question5 = int(input(Fore.BLUE + "What port does Domain Name System use? :"))
    if question5 == 53:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question5 = int(input(Fore.BLUE + "What port does Domain Name System use? :"))
            if question5 == 53:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Sixth question starts here
try:
    question6 = int(input(f"{Fore.BLACK}{Back.WHITE}What port does Tacas use? :"))
    if question6 == 49:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question6 = int(input(f"{Fore.BLACK}{Back.WHITE}What port does Tacas use? :"))
            if question6 == 49:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Seventh question starts here
question7 = input(Fore.WHITE + "Is Tacas TCP or UDP? :")
if question7 == "TCP":
    print("Good job!")
    score = (score + 1)
    print(f"Your current score is : {score}")
    print("########## :-) ##################### :-) ##################### :-) ###########")
else:
    print("That's not it")
    print(f"Your current score is: {score}")
    print("########## :-( ##################### :-( ##################### :-( ###########")
# There is no need for a error exception here since a number can be digested as a string and won't trigger an error
# Eighth question starts here
try:
    question8 = int(input(Fore.MAGENTA + "What port does Trivial File Transfer Protocol use? :"))
    if question8 == 69:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question8 = int(input(Fore.MAGENTA + "What port does Trivial File Transfer Protocol use? :"))
            if question8 == 69:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Ninth question starts here
try:
    question9 = int(input(Fore.LIGHTRED_EX + "What port does Link Local Multicast Name Resolution use? :"))
    if question9 == 5355:
        print("Good job!")
        score = (score + 1)
        print(f"Your current score is : {score}")
        print("########## :-) ##################### :-) ##################### :-) ###########")
    else:
        print("That's not it")
        print(f"Your current score is: {score}")
        print("########## :-( ##################### :-( ##################### :-( ###########")
except ValueError:
    print("Don't try to break my code man, Only numbers here")
    while ValueError == ValueError:
        try:
            question9 = int(input(Fore.LIGHTRED_EX + "What port does Link Local Multicast Name Resolution use? :"))
            if question9 == 5355:
                print("Good job!")
                score = (score + 1)
                print(f"Your current score is : {score}")
                print("########## :-) ##################### :-) ##################### :-) ###########")
                break
            else:
                print("That's not it")
                print(f"Your current score is: {score}")
                print("########## :-( ##################### :-( ##################### :-( ###########")
                break
        except ValueError:
            print("Don't try to break my code man, Only numbers here")
# Tenth question starts here
question10 = input(Fore.LIGHTBLUE_EX + "Which Team is the fun team? red or blue?")
if question10 == "red":
    print("Of course silly!!")
    score = (score * 2)
    print(f"Your current score is : {score}")
    print("########## You are awesome ##################### You are awesome ##################### You are awesome ###########")
else:
    print("Buuuuhhhh Boring team Buuuhhhhh")
    score = (score + 1)
    print(f"Your current score is : {score}")
    print("########## Zzz ##################### Zzz ##################### Zzz ###########")
if score == 18:
    print(f"Your Final score is {score}")
    print(f"{Fore.BLACK}{Back.YELLOW}This Program was powered by the knowledge collected from Travis Cafecito Lockman and Alex Garcia! Thank you Guys!")
    print(Back.YELLOW + "###### 1.1.1.1 If you see this message you achieved a perfect score! It doesn't get better than that! Teddy would be proud of you! ######## ")
    print(Back.YELLOW + "Well deserved")
elif score == 10:
    print(f"Your Final score is {score}")
    print(f"{Fore.BLACK}{Back.YELLOW}This Program was powered by the knowledge collected from Travis Cafecito Lockman and Alex Garcia! Thank you Guys!")
    print(f"{Fore.BLACK}{Back.RED}##### if you see this message you achieved a perfect score but chose the wrong color of team !>:(!")
else:
    print(f"Your Final score is {score}")
    print(f"{Fore.BLACK}{Back.YELLOW}This Program was powered by the knowledge collected from Travis Cafecito Lockman and Alex Garcia! Thank you Guys!")
