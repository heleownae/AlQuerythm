def solution(survey, choices):
    result = []
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    # 각 선택지에 따른 점수 배정
    points = {
        1: (0, 3),  
        2: (0, 2),  
        3: (0, 1),  
        4: (0, 0),  
        5: (1, 0),  
        6: (2, 0),  
        7: (3, 0)}
    
    for i in range(len(survey)):
        s1, s2 = survey[i][0], survey[i][1]  
        choice = choices[i]  
        
        if choice >= 5:  
            score[s2] += points[choice][0]  
        elif choice <= 3: 
            score[s1] += points[choice][1] 
    
    # 최종 성격 유형 결정    
    for mbti in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        type1, type2 = mbti
        if score[type1] > score[type2]:
            result.append(type1)
        elif score[type1] < score[type2]:
            result.append(type2)
        else:  
            result.append(min(type1, type2))
    
    return ''.join(result)
