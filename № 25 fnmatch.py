from fnmatch import fnmatch as mask

for x in range(50068, 10**10 + 1, 50068):
    s_x = str(x)
    if mask(s_x, '9?979*8') and ('0' in s_x):
        print(x, x // 50068)