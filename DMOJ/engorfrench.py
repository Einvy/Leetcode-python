n = int(input())
tcount = 0
scount = 0
for line in range(n):
    text = input()
    for letters in text:
     if letters == "S" or letters == "s":
        scount += 1
     elif letters == "T" or letters == "t":
        tcount += 1
if tcount > scount:
    print("English")
else:
    print("French")
