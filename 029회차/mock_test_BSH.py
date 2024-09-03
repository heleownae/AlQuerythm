def solution(answers):
    # 최대 10000개의 찍기 번호 리스트 만들기
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000

    # 정답 수 리스트
    result = [0,0,0]

    for i,j in enumerate(answers):
        if a[i]==j:
            result[0] += 1
        if b[i]==j:
            result[1] += 1
        if c[i]==j:
            result[2] += 1

    # 최대로 맞은 사람들을 필터링
    max_result = max(result)

    return [i+1 for i,j in enumerate(result) if j == max_result]
