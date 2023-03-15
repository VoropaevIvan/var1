file = open("107_27_B.txt")
n, k = [int(x) for x in file.readline().split()]

a = [0] * n
for i in range(n):
    a[i] = int(file.readline())

pr = [0] * (n + 1)
for i in range(1, n + 1):
    pr[i] = pr[i - 1] + a[i - 1]

inf = 10 ** 20
s_k = [-inf] * (n + 1)
for i in range(k, n + 1):
    s_k[i] = pr[i] - pr[i - k]

ans = 0
max_68 = [-inf] * 68

for j in range(k, n + 1):
    aj = s_k[j]
    ai = max_68[(68 - aj % 68) % 68]
    if ai != -inf and ai + aj > ans:
        ans = ai + aj

    if s_k[j + 1 - k] > max_68[s_k[j + 1 - k] % 68]:
        max_68[s_k[j + 1 - k] % 68] = s_k[j + 1 - k]
print(ans)


        
    



