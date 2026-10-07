n = int(input())
values = list(map(int, input().split()))
expectedtotal = 0

for number in range(1, n + 1):
    expectedtotal += number
actualtotal = sum(values)

print(expectedtotal - actualtotal)
