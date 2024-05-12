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
