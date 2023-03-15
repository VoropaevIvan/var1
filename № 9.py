f = open('9.txt')
otv = 0
for s in f:
    a = [int(x) for x in s.split()]
    a_p = []
    a_n = []

    for x in a:
        if a.count(x) == 1:
            a_n.append(x)
        else:
            a_p.append(x)
    if len(a_n) == 3 and len(a_p) == 3 and len(set(a_p)) == 1:
        if sum(a_n) / len(a_n) < sum(a_p):
            otv += 1
print(otv)

