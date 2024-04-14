# 라이브러리 미사용
n = int(input())
result = [i for i in range(1, n+1)]

while len(result) > 1:
    result.pop(0)
    result.append(result.pop(0))
print(result[0])

# 라이브러리 사용
from collections import deque

n = int(input())
result = deque(range(1, n+1))

while len(result) > 1:
    result.popleft()
    result.append(result.popleft())

print(result[0])
