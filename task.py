# GLOBAL VARIABLES
emplCode = ""
validEmplCode = False

# MAIN PROGRAM

# ==> rearrange the lines to validate an input for length and uppercase
# (do not change the indentation)

print("Your code {} was accepted".format(emplCode))
        print("Invalid code, try again...")
    else:
        validEmplCode = True
while validEmplCode == False:
    if len(emplCode) == 5 and emplCode.isupper():
    emplCode = input("Enter 5 character uppercase employee code: ")

