"""Lab Objective: Save a ping output to a file with Python’s OS module."""

import os

file_name = input("Choose a filename: ")
os.system(r"ping 8.8.8.8 >> " + file_name + ".txt")

with open(file_name + ".txt","r") as file:
    if "ms" in file.read():
        print("You have an internet connection")
    else:
        print("You don't have an internet connection")

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
