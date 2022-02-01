# Example written by Travis Lockman at Genaro's Request
# O_o tHe pAcKeTs nEvEr LiE o_O #

title = "Genaro's SSN Stealer"
author = "by Travis L"

def ssn(name, dob, ssn):
    print(title)
    print(author)
    print("Your name: " + str(name))
    print("Your birthday: " + str(dob))
    print("Your ssn: " + str(ssn))

askname = input("Please enter your name: ")
askdob = input("Please enter your DOB")
askssn = input("Please enter your SSN")

output = ssn(str(askname),str(askdob),str(askssn))

print(output)
