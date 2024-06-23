def solution(n):
    if n == 1:
        return 1
    
    answer = 0
    
    for i in range(1, int(n**0.5)+1):  # range 함수에 float형은 오류 발생. int형으로 변경해줘야 함.
        if n % i == 0:
            answer += i
            if (n//i) != i:
                answer += n//i
    return answer
