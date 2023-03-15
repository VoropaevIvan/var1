alf_8 = '01234567'
count = 0
for i1 in '1234567':
    for i2 in alf_8:
        for i3 in alf_8:
            for i4 in alf_8:
                for i5 in alf_8:
                    for i6 in alf_8:
                        s = i1 + i2 + i3 + i4 + i5 + i6
                        if s.count('6') == 2:
                            s = s.replace('1', 'н').replace('3', 'н').replace('5', 'н').replace('7', 'н')
                            if ('н6' not in s) and ('6н' not in s):
                                count += 1
print(count)
