from itertools import product

otv = 0
a = product('01234567', repeat=6)
for x in a:
    s = ''.join(x)
    if s[0] != '0' and s.count('6') == 2:
        s = s.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
        if ('6н' not in s) and ('н6' not in s):
            otv += 1
print(otv)
