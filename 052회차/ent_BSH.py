s="[)(]"
lit=list(s)
x=len(s)
cnt=0
ent_1 = [']',')','}']
ent_2 = ['[','(','{']

for i in range(x):
    ent = lit.pop(0)
    lit.append(ent)
    print(lit)

    for a,b in enumerate(lit):
        if a%2 == 0 and b in ent_1:
            break
        if a%2 == 1 and b in ent_2:
            break
    cnt+=1

cnt
