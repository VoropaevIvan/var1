f = open('17.txt')
a = []
for s in f:
    a.append(int(s))

a_68 = []
for x in a:
    if abs(x) % 100 == 68:
        a_68.append(x)

min_68 = min(a_68)
count = 0
max_sum = -10000000000
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]

    if (abs(first) % 100 == 68) + (abs(second) % 100 == 68) == 1:
        if first**2 + second**2 >= min_68**2:
            count += 1
            max_sum = max(max_sum, first**2 + second**2)

print(count, max_sum)
print(min_68)