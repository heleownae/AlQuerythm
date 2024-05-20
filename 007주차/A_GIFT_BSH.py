test = list(map(int,input().split()))
first = test.pop(0)
answer = [i+1 for i in range(min(test))]
answer.sort(reverse=True)
result=[]
for i in answer:
    if ((i)**3)*first <= test[0]*test[1]*test[2]:
        result.append(i)
print(max(result))

# 예제4번 오류...ㅠ
