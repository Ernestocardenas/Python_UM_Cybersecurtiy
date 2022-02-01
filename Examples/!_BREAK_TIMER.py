# Travis' Break Timer, inspired by Tyrel Barstow
# O_o tHe pAcKeTs nEvEr LiE o_O #
# April 2021

from datetime import datetime
import random
import os
import time

# Getting the break return time.
return_time = input("Please enter the time to return from break: ")
wv = input("Display quotes? (y/n): ").lower()

# Creating a tuple that contains all of our quotes.
Quotes = (
            "The greatest glory in living lies not in never falling, but in rising every time we fall. "
            "-Nelson Mandela\n\n",
            "The way to get started is to quit talking and begin doing. -Walt Disney\n\n",
            "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt\n\n",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life,"
            " you'll never have enough. -Oprah Winfrey\n\n",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
            " -James Cameron\n\n",
            "Life is what happens when you're busy making other plans. -John Lennon\n\n",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa\n\n",
            "When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt\n\n",
            "Always remember that you are absolutely unique. Just like everyone else. -Margaret Mead\n\n",
            "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt\n\n",
            "Tell me and I forget. Teach me and I remember. Involve me and I learn. -Benjamin Franklin\n\n",
            "The best and most beautiful things in the world cannot be seen or even touched - "
            "they must be felt with the heart. -Helen Keller\n\n",
            "It is during our darkest moments that we must focus to see the light. -Aristotle\n\n",
            "Whoever is happy will make others happy too. -Anne Frank\n\n",
            "Do not go where the path may lead, go instead where there is no path and leave a trail. "
            "-Ralph Waldo Emerson\n\n",
            "The only impossible journey is the one you never begin. -Tony Robbins\n\n",
            "Life is really simple, but we insist on making it complicated. -Confucius\n\n",
            "Love the life you live. Live the life you love. -Bob Marley\n\n",
            "Live as if you were to die tomorrow. Learn as if you were to live forever. – Mahatma Gandhi\n\n",
            "We must not allow other people’s limited perceptions to define us. – Virginia Satir\n\n",
            "This above all: to thine own self be true. – William Shakespeare\n\n",
            "If opportunity doesn’t knock, build a door. – Milton Berle\n\n",
            "Strive not to be a success, but rather to be of value. – Albert Einstein\n\n",
            "There will always eventually be an error. - Tyrel Barstow\n\n",
            "There is no spoon. -Neo\n\n",
            "Do or do not, there is no try. -Master Yoda\n\n",
            "Everybody learns differently and everybody gets to a certain point from a different "
            "direction. - Stan Lee\n\n"
         )

# Getting the length of our tuple.
QuotesLength = len(Quotes) - 1

# I always make my infinite loops flashy.
Tacos = 100
Everything = 99
while Tacos > Everything:
    # Cleaning up the screen.
    os.system("cls")
    # Using datetime to get the current time.
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


    # Converting to a 12 hour.
    time_list = current_time.split(":")
    counter = 0

    #Need integers
    for x in range(1):
        time_list[x] = int(time_list[x])

    #Determining AM or PM
    if time_list[0] > 12:
        time_list[0] = time_list[0] - 12
        tod = "PM"
    else:
        tod = "AM"

    #Back to strings.
    for x in range(1):
        time_list[x] = str(time_list[x])

    #Putting it all together.
    return_time_o = (f"Please return from break at:\n {return_time}\n\n")
    current_time = (f"The Current Time Is:\n {time_list[0]}:{time_list[1]} {tod}\n\n")
    listpos = random.randint(0, QuotesLength)
    CurrentQuote = Quotes[listpos]

    print("#####################################################################################")
    print("              o_O Travis' Break Timer with Quotes for Life O_o")
    print("\n\n\n")
    if wv == "n":
        print(return_time_o, current_time)
    else:
        print(CurrentQuote, return_time_o, current_time)
    time.sleep(15)
    os.system("cls")

    #Getting Fancy
    logo = """
        .===============================================================================.
        |                                .::::::::::.                                   |
        |                              .::``::::::::::.                                 |
        |                              :::..:::::::::::                                 |
        |                              ````````::::::::                                 |
        |                      .::::::::::::::::::::::: iiiiiii,                        |
        |                   .:::::::::::::::::::::::::: iiiiiiiii.                      |
        |                   ::::::::::::::::::::::::::: iiiiiiiiii                      |
        |                   ::::::::::::::::::::::::::: iiiiiiiiii                      |
        |                   :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii                      |
        |                   :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii                      |
        |                   `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`                      |
        |                      `:::::: iiiiiiiiiiiiiiiiiiiiiii`                         |
        |                              iiiiiiii,,,,,,,,                                 |
        |                              iiiiiiiiiii''iii                                 |
        |                              `iiiiiiiiii..ii`                                 |
        |                                `iiiiiiiiii`                                   |
        |                                                                               |
        |                      ____        _   _                                        |
        |                     |  _ \ _   _| |_| |__   ___  _ __                         |
        |                     | |_) | | | | __| '_ \ / _ \| '_ \                        |
        |                     |  __/| |_| | |_| | | | (_) | | | |                       |
        |                     |_|    \__, |\__|_| |_|\___/|_| |_|                       |
        |                            |___/                                              |
        |                           We will be back shortly...                          |
        .===============================================================================.
            """
    print(logo)
    time.sleep(5)