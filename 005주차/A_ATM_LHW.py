N = int(input())
P = list(map(int, input().split()))

P.sort()
tot = 0
for i in range(N):
    tot += P[i] * (N - i)

print(tot)