x = int(input())
n = int(input())
value = 0
for val in range(n):
    other = int(input())
    value = value + x - other
print(value + x)
