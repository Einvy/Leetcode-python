a = int(input())
acount = 1
bcount = 0


for press in range(a):
    newacc = bcount
    newbcount = acount + bcount

    acount = newacc
    bcount = newbcount

print(acount, bcount)
