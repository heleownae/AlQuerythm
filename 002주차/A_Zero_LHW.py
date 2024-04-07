# 백준 10773 제로


# 1 (3280ms)
stack = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))


# 2 (76ms)
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))