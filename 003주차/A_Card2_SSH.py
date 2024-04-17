input()

a = [i for i in range(1, n+1)]
while len(a) > 1:
    a.pop(0)
    c = a.pop(0)
    a.append(c)
    
a
