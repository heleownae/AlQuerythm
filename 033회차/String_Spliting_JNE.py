def solution(s):
    answer = 0
    
    while s:
        fst = s[0]
        # 단어가 분해될 때마다 count 리셋시켜 주기
        count_same = 0
        count_diff = 0
        
        for snd in s:
            if fst == snd :
                count_same += 1
            else :
                count_diff += 1
            
            if count_same == count_diff:
                answer += 1
                s = s[len(s[:count_same + count_diff]): ]
                break
  # 더 이상 읽을 글자가 없을 경우
        else:
            answer += 1  
            break    
    return answer
