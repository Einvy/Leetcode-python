c = int(input())
correctcount = 0
studentanswer = ""
for q in range(c):
    studentanswer += input()
for q in range(c):
    answer = input()
    if studentanswer[q] == answer:
        correctcount += 1
print(correctcount)
