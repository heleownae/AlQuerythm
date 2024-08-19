def solution(s):
    # 각 글자의 마지막 위치를 기록하는 딕셔너리
    last = {}
    # 결과 리스트 초기화
    result = []
    
    for i, J in enumerate(s):
        # 현재 문자의 마지막 위치가 기록되어 있는지 확인
        if J in last:
            # 같은 글자가 이전에 나왔다면 현재 인덱스와 마지막 위치의 차이를 계산
            result.append(i - last[J])
        else:
            # 처음 나왔다면 -1 추가
            result.append(-1)
        
        # 현재 문자의 위치 업데이트
        last[J] = i
    
    return result
