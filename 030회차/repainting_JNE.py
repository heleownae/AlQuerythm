def solution(n, m, section):
    section.sort()
    # 롤러로 칠하는 횟수를 세기 
    answer = 0
    # 롤러 시작 위치
    paint = 0
    
    for s in section:
        # 현재 위치가 다시 칠해야 할 구역의 시작 위치보다 크거나 같으면 롤러를 새로 칠함
        if s >= paint:
            answer += 1
            # 위치 재조정
            paint = s + m - 1  
    
    return answer
