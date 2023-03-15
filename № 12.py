def prime(x):
    for j in range(2, x):
        if x % j == 0:
            return 0
    return 1


for n in range(0, 10):
    sum_ = 39 + 2 * (2 * n + 39)
    print(n, sum_, prime(sum_))
