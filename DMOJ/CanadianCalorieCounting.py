a = int(input())
b = int(input())
c = int(input())
d = int(input())
calories = 0

if a == 1:
    calories += 461
elif a == 2:
    calories += 431
elif a == 3:
    calories += 420
elif a == 4:
    calories += 0

if b == 1:
    calories += 100
elif b == 2:
    calories += 57
elif b == 3:
    calories += 70
elif b == 4:
    calories += 0

if c == 1:
    calories += 130
elif c == 2:
    calories += 160
elif c == 3:
    calories += 118
elif c == 4:
    calories += 0

if d == 1:
    calories += 167
elif d == 2:
    calories += 266
elif d == 3:
    calories += 75
elif d == 4:
    calories += 0
print(f"Your total Calorie count is {calories}.")

