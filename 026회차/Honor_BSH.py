def solution(k, score):
    answer = []
    result = []
    for i in range(len(score)):
        if i >= k:
            if score[i] >= answer[0]:
                answer.remove(answer[0])  # 최소값 제거
                answer.append(score[i])    # 새로운 점수 추가
                answer.sort()
            result.append(min(answer))  # 최소값을 추가하는 부분
        else:
            answer.append(score[i])
            answer.sort()
            result.append(min(answer))

    return result
