n = input()
honi = "HONI"
spot = 0
honicount = 0
for letter in n:
    if letter == honi[spot]:
        spot += 1
        if spot == 4:
            honicount += 1
            spot = 0
print(honicount)
