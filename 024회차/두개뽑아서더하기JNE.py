def solution(numbers):
    answer = []    
    # 두 개의 수를 뽑아 더하기
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            value = numbers[i] + numbers[j]
            # 이미 리스트에 없는 경우에만 추가
            if value not in answer:
                answer.append(value)    
    answer.sort()
    return answer
