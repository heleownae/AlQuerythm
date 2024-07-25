def solution(n):
    answer=[]
    while True:
        result = divmod(n,3)
        answer.append(result[1])
        if result[0] == 0:
            break
        n = result[0]
    ten = [i for i in range(len(answer)-1,-1,-1)]
    return sum([answer[i]*3**ten[i] for i in range(len(answer))])
