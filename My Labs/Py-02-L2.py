name = input("What is your name? ")  #Take name input
age = input("What is your age? ")  #takes age input

age = int(age)  #converts age from string to int
print(f"Hello {name}, your age is {age}.")  #prints name and age

if age >= 21:  #compares age input to 21
    print("You can buy an alcoholic beverage") #if age input is under 21
else:
    print("You cannot buy an alcoholic beverage") #if age input is 21 or over





