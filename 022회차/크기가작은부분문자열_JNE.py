def solution(t, p):
    answer = 0
    a = len(p)
    # p문자열 길이와 같을 때까지만 반복
    for b in range(len(t) - a + 1):
    # 인덱스를 이용해 p 문자열 길이만큼 t 문자열 불러와서 크기 비교
        if int(t[b:b + a]) <= int(p):
            answer += 1
    return answer
