file = open("26.txt")

n = int(file.readline())
a = [int(x) for x in file]

a.sort()
a = [0] + a
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]

for i in range(n):
    kol_6 = i // 6
    kol = i - kol_6
    
    s_6 = 0
    for j in range(i, kol, -1):
        s_6 += a[j]
    

    # s_bez_sk = s[kol]
    # s_6 = s[i] - s_bez_sk

    if s[kol] + 0.5 * s_6 > 100000:
        break
    summ = s[kol] + 0.5 * s_6
    count = i
print(count, 100000 - summ)