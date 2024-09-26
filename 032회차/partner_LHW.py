def solution(X, Y):
    answer = ''.join(
        str(i) * min(X.count(str(i)), Y.count(str(i)))
        for i in range(9, -1, -1))
    
    if not answer:
        # 공통 숫자 X
        return '-1'
    elif set(answer) == {'0'}:
        # 공통 숫자 0
        return '0'
    else:
        # 그 외는 문자열 반환
        return answer
