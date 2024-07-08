def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            a = absolutes[i] * 1
            answer += a
        else :
            a = absolutes[i] * (-1)
            answer += a
    return answer
    
# 줄이기1 - 실패    
def solution(absolutes, signs):
# else 블록이 for 루프의 반복 조건과 관계없이 실행됨
# for-else 구조는 for 루프가 정상적으로 끝났을 때(break 문으로 중간에 빠져나오지 않고) else 블록이 실행
    return sum(absolutes[i] for i in range(len(absolutes)) if signs[i] else -absolutes[i])
  
# 줄이기2 - 성공    
def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))
