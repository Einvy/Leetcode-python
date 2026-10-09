password = input()
upperletter = 0
lowerletter = 0
digit = 0
# Use count maybe upper as well?
for letters in password:
    if letters.isupper():
        upperletter += 1
    elif letters.islower():
        lowerletter += 1
    elif letters.isdigit():
        digit += 1
if len(password) < 8 or len(password) > 12:
    print("Invalid")
elif upperletter >= 2:
    if lowerletter >= 3:
        if digit >= 1:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
