#def f(start, end):
    #d = [0] * 100
    #d[start] = 1
    #for i in range(start + 1, end + 1):
        #d[i] = d[i - 1] + d[i - 2] + d[i - 3]
        #if i % 4 == 0:
            #d[i] += d[i // 4]
        #if i == 58:
            #d[i] = 0
    #return d[end]

#print(f(38, 45) * f(45, 68))

def f(x, start):
    if x == start:
        return 1
    if x < start:
        return 0
    if x == 58:
        return 0
    s = f(x - 1, start) + f(x - 2, start) + f(x - 3, start)
    if x % 4 == 0:
        s += f(x // 4, start)
    return s
print(f(45, 38) * f(68, 45))
    
        
    


