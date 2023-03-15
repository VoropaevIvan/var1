file = open("24.txt")
s = file.readline()

n = len(s)
d = [0] * (n + 1)
ans = 0
for i in range(3, n + 1):
    si = i - 1
    if s[si] in "OA" and s[si - 2] in "CDF":
        d[i] = d[i - 3] + 1
        ans = max(ans, d[i])
    else:
        d[i] = 0
print(ans)


