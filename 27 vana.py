f = open("107_27_B.txt")
n, k = [int(s) for s in f.readline().split()]

a = [0] + [int(s) for s in f]
otv = -1

pref = [0]*(n+1)
pref[0] = 0
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + a[i]

d = [-1]*68
for i in range(1 + k, n - k + 1 + 1):
    pred_sum = pref[i - 1] - pref[i - k - 1]
    d[pred_sum % 68] = max(pred_sum, d[pred_sum % 68])

    right_sum = pref[i+k-1] - pref[i-1]

    if d[(68 - right_sum % 68)%68] != -1:
        otv = max(otv, d[(68 - right_sum % 68)%68] + right_sum)

print(otv)


