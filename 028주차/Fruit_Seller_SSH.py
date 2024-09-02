def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m #정렬해준 뒤 m간격으로 첫번째 요소만 추출, 이를 m으로 곱해줌
