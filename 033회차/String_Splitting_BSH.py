def solution(s):
    first = 0
    other = 0
    result = 0

    for char in s:
        if first == other:  # 균형 상태일 때
            first = 1  # 첫 번째 문자의 카운트를 시작
            current_char = char
        elif char == current_char:  # 두 번째 문자부터 실행
            first += 1
        else:
            other += 1

        if first == other:  # 균형 체크
            result += 1
            first = 0  # 같아지면 리셋
            other = 0  # 같아지면 리셋

    # 남은 문자 처리: if 뭐라도 남아있으면
    if first > 0 or other > 0:
        result += 1

    return result
