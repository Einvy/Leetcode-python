with open("teleport.in", "r") as file:
    a,b,c,d = map(int, file.read().split())
answer = 0
one = abs(a - b)
two = abs(a - c) + abs(d - b)
three = abs(a - d) + abs(c - b)
if one < two and one < three:
    answer = one
elif two < one and two < three:
    answer = two
elif three < one and  three < two:
    answer = three

with open("teleport.out", "w") as file:
    file.write(str(answer) + "\n")
