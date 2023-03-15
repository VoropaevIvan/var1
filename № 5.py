for N in range(1, 100000):
    s_2 = bin(N)[2:]
    if s_2.count('1') % 2 == 0:
        s_2 = s_2 + '0'
        s_2 = '101' + s_2[3:]
    else:
        s_2 = s_2 + '11'
        s_2 = '10' + s_2[2:]

    R = int(s_2, 2)
    if R > 68:
        print(N)
        break
