a = int(input())
count = 0
for __ in range(a):
    word = input()
    if len(word) > 10:
        count = len(word) - 2
        print(f"{word[0]}{count}{word[-1]}")
    else:
        print(word)
