def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score) // m):
        box = score[m*i : m*(i+1)]
        answer += box[-1] * m
        
    return answer

"""
1. 점수 내림차순으로 정렬
2. 상자에 넣을 사과를 m개씩 각각 분리
3. 가장 작은 점수(인덱스 -1)의 사과와, 한 상자에 들어갈 사과 수(m)를 곱하기
"""
