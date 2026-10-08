a = int(input())
b = int(input())
c = int(input())

if a > b and a < c:
    print(a)
elif a > c and a < b:
    print(a)
elif b > a and b < c:
    print(b)
elif b > c and a > b:
    print(b)
elif c > b and c < a:
    print(c)
elif c > a and c < b:
    print(c)
