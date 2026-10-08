a = int(input())
b = input()
c = input()
countone = 0
for vals in range(len(b)):
        if b[vals] == "C" and c[vals] == "C":
            countone += 1
print(countone)
