def solution(n):
    answer = ""
    
    while n >= 1:
        answer += str(n % 3)    # 3으로 나눈 나머지를 문자열로 저장
        n = n // 3              # 3으로 나눈 몫으로 업데이트 후 while 반복
        
        # answer = answer[::-1]
    
    return int(answer, 3)       # 10진법으로 변환 후 return
