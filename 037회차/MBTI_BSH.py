def solution(survey, choices):
    score={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    mbti={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    mbti_list=['RT','CF','JM','AN']
    result=[]

    for i,e in enumerate(survey):
        choice = choices[i]  # 두 번 이상 쓰이니까 변수저장 재사용
        if choices[i] <= 3:
            mbti[e[0]]=mbti[e[0]]+score[choice]
        else:
            mbti[e[1]]=mbti[e[1]]+score[choice]

    for  word in mbti_list:
        if mbti[ word[0]] > mbti[ word[1]]:
            result.append( word[0])
        elif mbti[ word[0]] < mbti[ word[1]]:
            result.append( word[1])
        else:
            result.append(min( word[0], word[1]))

    return ''.join(result)
