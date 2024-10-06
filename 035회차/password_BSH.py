def solution(s, skip, index):
    search=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result=[]

    for i in skip:
        search.remove(i)  # skip 해당 알파벳 제거

    for i in s:
        answer=search.index(i)+index  # 인덱스 갱신
        while answer>=len(search):  # 초과 인덱스 처리
            answer=answer-len(search)
        result.append(search[answer])  # 새로운 변수에 할당

    return ''.join(result)
