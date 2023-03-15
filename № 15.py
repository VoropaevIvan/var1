for A in range(1, 10**10):
    flag_A = 1
    for x in range(1, 1_000 + 1):
        f = ((x % 2 == 0) <= (x % 13 != 0)) or (x + A >= 1000)
        if f == 0:
            flag_A = 0
            break

    if flag_A == 1:
        print(A)
        break
