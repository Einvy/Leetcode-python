n = input()
acount = 0
ccount = 0

for measure in n.split("|"):
    letter = measure[0]

    if letter in "ADE":
        acount += 1
    elif letter in "CFG":
        ccount += 1

if acount > ccount:
    print("A-mol")
elif ccount > acount:
    print("C-dur")
else:
    if n[-1] == "A":
        print("A-mol")
    else:
        print("C-dur")
