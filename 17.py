file = open("17.txt")


a = [int(x) for x in file]
min_68 = min([x for x in a if abs(x) % 100 == 68])

s = [a[i]**2 + a[i - 1]**2 for i in range(1, len(a)) if ((abs(a[i]) % 100 == 68) != (abs(a[i - 1]) % 100 == 68)) and (a[i] ** 2 + a[i - 1]**2 >= min_68 ** 2)]
print(len(s), max(s))