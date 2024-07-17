def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

'''
# 예전 제출 코드
def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        pass
    else:
        answer = False
    return answer

# 논리연산자의 결과는 불리언 형식이라서 if문 필요 없음
'''
