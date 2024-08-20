def solution(k, score):
# 명예의 전당 리스트
    honor = []  
    # 매일 발표된 최하위 점수를 저장할 리스트
    result = []  

    for s in score:
        # 현재 점수를 명예의 전당에 추가
        honor.append(s)
        # 명예의 전당에서 상위 k개의 점수로 정렬
        # 내림차순 정렬
        honor.sort(reverse=True)  

        # 명예의 전당의 크기가 k를 초과하면 가장 낮은 점수를 제거
        if len(honor) > k:
        # 가장 낮은 점수 제거
            honor.pop()  

        # 현재 명예의 전당의 최하위 점수를 추가
        # 가장 낮은 점수는 마지막 요소
        result.append(honor[-1])  

    return result
