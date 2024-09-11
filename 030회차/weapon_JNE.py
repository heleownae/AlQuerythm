def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        # 약수 개수 계산
        count = 0
        # 약수는 짝수로 존재
        for i in range(1, int(num**0.5) + 1):
            # i가 num의 약수 인지 확인
            if num % i == 0:
                count += 1  
                # i가 num의 약수일 때, num // i도 약수임
                if i != num // i:
                    count += 1  # n // i도 약수

        # 공격력 제한수치
        if count > limit:
            answer += power
        else:
            answer += count
            
    return answer
