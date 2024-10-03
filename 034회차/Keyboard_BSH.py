# 절반 틀림
def solution(keymap, targets):
    answer=[]

    def function(list):
        result=[]
        for i in list:
            num=[keymap[e].find(i) for e in range(len(keymap))]
            if max(num)==-1 and min(num)==-1:
                result.append(-1)
            else:
                num = [i for i in num if i != -1]
                result.append(min(num)+1)
        return sum(result)

    for i in targets:
        answer.append(function(i))

    return answer
