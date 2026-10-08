n = input()
val = 1
for letters in n:
    if letters == "A":
        if val == 1:
            val = 2
        elif val == 2:
            val = 1
    elif letters == "B":
        if val == 2:
            val = 3
        elif val == 3:
            val = 2
    elif letters == "C":
        if val == 3:
            val = 1
        elif val == 1:
            val = 3
print(val)

# Could also do if letters == "A" and val == 1: 
#So that it takes up less lines.
