k, n ,w = map(int, input().split())
total = 0

for i in range(1, w + 1):
    total += i * k

friend = total - n

if friend < 0:
    friend = 0
print(friend)
