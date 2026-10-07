n = input()
count = 1
compare = 1

for letters in range(1, len(n)):
    if n[letters] == n[letters - 1]:
        count += 1
    else:
        count = 1
    if count > compare:
        compare = count
print(compare)
# for index, char in enumerate(n):
#
