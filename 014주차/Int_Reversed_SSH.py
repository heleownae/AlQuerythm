def solution(n):
    answer = ""
    for x in reversed(list(sorted(str(n)))):
        answer += x
    return int(answer)




#정답
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))


#join 예시
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return ("a".join(ls))

#=>	실행한 결괏값 "8a7a3a2a1a1"이 기댓값 873211과 다릅니다.
