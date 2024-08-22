def solution(k, score):
    honor = []
    answer = []
    
    for s in score:
        honor.append(s)
        honor.sort(reverse=True)

        if len(honor) > k:
            honor.pop()
        
        answer.append(honor[-1])
    
    return answer
