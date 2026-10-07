n = int(input())
solve = 0
for _ in range(n):
    values = input().split()
    total = 0
    for value in values:
        total += int(value)
    if total >= 2:
        solve += 1
print(solve)
