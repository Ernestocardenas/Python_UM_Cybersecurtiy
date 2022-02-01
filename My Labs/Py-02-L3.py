print("PY-02-L3")  # Lab 3

grade = input("Enter a grade: ")  # grade input not used
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Letter grade: A")

elif grade >= 80:
    print("Letter grade: B")

elif grade >= 70:
    print("Letter grade: C")

elif grade >= 60:
    print("Letter grade: D")

else:
    print("ERROR: Grade cannot be negative numbers or words.\n")

    print("Press 'ENTER' To exit Program")
    