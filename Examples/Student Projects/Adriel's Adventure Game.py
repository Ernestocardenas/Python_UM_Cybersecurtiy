# Blood Pressure Monitor
# Adriel
# UM Cyber Bootcamp Student May 2021

import hello

# universal variables
ammo = 15
the_force = 0
lives = 5

print("Hello Traveler, I see that you are interested in an ... Adventure")
hello.sleep(3)
print("Because this shop has been affected by 'rona, we can only provide two different adventures \n")
hello.sleep(3)
answer = input("Are you interested? (yes/no): \n").lower()

if answer == "yes":
    print("- Wonderful. As I said, I need to find the two pills for your trip. Give me a sec to find them ...")
    hello.sleep(4)
    print("- searching for pills...")
    hello.sleep(3)
    print("Allrighty, I found them, so... We got a red pill and a blue pill ")
    hello.sleep(3)
    print("Yes, we did this on purpose, it's helps with marketing ...")
    hello.sleep(3)
    pill_decision = input("Which will you choose (red/blue): \n").lower()

    if pill_decision == "blue":
        print("Well well well, I'm gonna ask Neo to come get you cuz that's outside my paycheck \n"
              "Just a word of advice, avoid Agent Smith, he's kind of a douche. See ya ...")
    elif pill_decision == "red":
        print("Nice, I like this one.")
        hello.sleep(2)
        print("Now, you are going to go on a trip (on my favorite rocket ship...)")
        hello.sleep(3)
        print("You will hear my voice the entire hello in your head, kind of like in a video game,")
        hello.sleep(3)
        print("Yu wake up, It will feel a lot like a dream, ")
        hello.sleep(3)
        print("See you on the other side and hopefully you will survive this trip ")
        hello.sleep(3)
        print("Here we go... \n")

        hello.sleep(5)
        print("Alright, I'm ready ... \n")
        hello.sleep(2)
        print("Let me explain what's going on: You are on an dark forest,")
        hello.sleep(3)
        print("and your objective is to reach the light alive, preferably with all your limbs on you")
        hello.sleep(3)
        weapon_decision = input("Now, for your decision: do you want weapon or not? (yes/no) (I would pick one if I were you): \n").lower()
        if weapon_decision == "yes":
            weapon_dict = ["Shotgun", "Lightsaber", "Waterbending", "AK-47"]
            print(weapon_dict)
            weapon_choice = input("Which weapon will you choose?: \n").lower()

            if weapon_choice == "Shotgun":
                print("Excellent choice Arnold (make sure Sara Connor doesn't find ya), your weapon has " + str(ammo) + " rounds")
                hello.sleep(3)
                print("Arnold is incredible, so he just wins automatically from being there, I mean come on, he's the Terminator...")
            elif weapon_choice == "lightsaber":
                print("- I see we have a padawan here ... Well, you will have to learn to dominate the force")
                hello.sleep(3)
                print("within you as you move forward. Your force level as of now is " + str(the_force) + ".")
                hello.sleep(3)
                print("And, at this point, you have " + str(lives) + " remaining")
                hello.sleep(4)
                print("- I see you are armed and ready ... why the robes for? Doesn't matter ")
                hello.sleep(3)
                print("Do you at least know to use the force to turn on that silly flashlight? Oh boy ...")
                hello.sleep(3)
                print("Let me explain something, over hello, you will need to eat, otherwise you will lose lives from starving.")
                hello.sleep(3)
                print("All right, you are going to need to find a way out, and find a master too")
                hello.sleep(4)
                print("You start walking and find yourself next to a river.")
                cross_river = input("Will you follow the river or cross it? (follow/cross): \n").lower()
                if cross_river == "follow":
                    print("- congrats! After a while of following the river, you come across a house.")
                    print("You need to find food soon,")
                    print("The house may contain a surprise, but you may also die... \n")

                    house_decision = input("Do you go to the house or continue on your way? (house/continue): ").lower()
                    if house_decision == "house":
                        print("See you in my house, nice it is. Padawans in search of a master, welcome in my house they are.")
                        hello.sleep(3)
                        print("learning the force \n")
                        hello.sleep(5)
                        print("Satisfy your hunger, this parcel of food, will. Safe travels I wish to you.")
                        hello.sleep(3)
                        print("The force is strong within you, young padawan.")
                        hello.sleep(3)
                        print("May the force be with you")

            elif weapon_choice == "Waterbending":
                print("A fine student from the descendants of the poles I see. You will need to find a teacher \n"
                      "And who knows, maybe you will be surprised along the way...")
                hello.sleep(2)
                print("Wait...")
                hello.sleep(3)
                print("Yea sorry, I did not finish this part of the code yet")
            elif weapon_choice == "AK-47":
                print("Excellent choice Rambo (don't let the alien hunt you down), your weapon has" + str(ammo) + "rounds")
                hello.sleep(2)
                print("Wait...")
                hello.sleep(3)
                print("Yea sorry, I did not finish this part of the code yet")
            else:
                print("I'm really sorry, I still didn't code for how to go back and choose the correct weapon")

        else:
            print("Well, I guess you are going barehanded ... \n"
                  "wait... \n"
                  "Actually, you lost the game already, there's no way you are going to get through the boss \n"
                  "yea, I'm going to count this trip as lost, I'll see you on the other side")

    else:
        print("Well, we can offer you a beer and then ask you to get out of this shop, \n"
              "...respectfully... \n "
              "we got other customers to serve still")

elif answer == "no":
    print("well, that's a shame, have a nice day in your regular life, and safe travels ")
    hello.sleep(3)
    print("............")
    hello.sleep(2)
    print("loser")
else:
    print("you really need to start following directions now")