"""Lab Objective: Understand how to work with nested lists and for loops together with the range function."""
classroom = []

for i in range(7):
    classroom.append([])
    for students in range(1,11):
        classroom[i].append(students)

print(classroom)

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
