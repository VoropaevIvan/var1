f = open('107_27_A.txt')
n, k = [int(s) for s in f.readline().split()]

a = [int(s) for s in f]
otv = -1

for i in range(0, n - k):
    for j in range(i + k, n-k):
        if (sum(a[i:i+k])+sum(a[j:j+k])) % 68 == 0:
            otv = max(otv, sum(a[i:i+k])+sum(a[j:j+k]))

print(otv, otv % 68)