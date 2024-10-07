def solution(s, skip, index):
    # 알파벳 리스트 생성 (a-z)
    search = [chr(i) for i in range(97, 123)]
    result = []

    # skip에 해당하는 알파벳 제거
    for i in skip:
        if i in search:
            search.remove(i)

    # 각 문자에 대해 새로운 문자 계산: 인덱스 초과 처리 포함
    for e in s:
        new_index = (search.index(e) + index) % len(search)
        result.append(search[new_index])

    return ''.join(result)
