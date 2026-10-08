n = int(input())
s = int(input())
diff = s - n
oldest = diff + s
if n == s:
    oldest = s
print(oldest)
