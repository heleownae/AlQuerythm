a = [int(input()) for i in range(int(input()))]
a.sort()
result = []
added = 0
for i in a:
    if len(result) == 0:
        result.append(i)
    else:
        result.append(added+i)
    added += i
print(sum(result))
