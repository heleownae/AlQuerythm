a = input()
cnt = input().split()
b = input()
card = input().split()
result = []
for i in card:
    num=0
    if i in cnt:
        while True:
            try:
                cnt.remove(i)
                num+=1
            except:
                result.append(str(num))
                break
    else:
        result.append('0')





from collections import Counter
a = input()
cnt = input().split()
b = input()
card = input().split()
class_counter = Counter(cnt)
result = []
for i in card:
    result.append(str(class_counter[i]))
print(*result)
