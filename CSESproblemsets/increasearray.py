n = int(input())
second = list(map(int, input().split()))
val = 0
for number in range(1, n):
    if second[number] < second[number - 1]:
        val += second[number - 1] - second[number]
        second[number] = second[number - 1]
print(val)


