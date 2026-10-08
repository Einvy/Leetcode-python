p = int(input())
b = int(input())
d = int(input())
# p is leftover b is paint. d is for sale of it.
# remaining paint sold for 1
total = int(p / b)
extra = int(p % b)
print((total * d) + extra)
