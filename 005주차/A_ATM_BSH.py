people = int(input())
answer = sorted(map(int, input().split()))
result = 0
added = 0

for i in answer:
    result+= i+added
    added += i

print(result)
