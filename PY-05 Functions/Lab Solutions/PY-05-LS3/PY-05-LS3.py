"""Lab Objective: Create global variables and try to make changes to them within a function."""

global_var = 5
changed_global_var = 20

def local_change():
    global_var = 10
    print("inside function global_var's value: ", global_var)
    global changed_global_var
    changed_global_var += 5
    print("inside function changed_global_var's value: ", changed_global_var)

local_change()
print("outside function global_var's value: ", global_var)
print("outside function changed_global_var's value: ", changed_global_var)


input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
