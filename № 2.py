print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (not (x <= w)) or (y <= z) or (not y)
                if f == 0:
                    print(x, y, z, w)
