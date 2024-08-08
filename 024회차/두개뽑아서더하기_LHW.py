def solution(numbers):
    zero = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            zero.add(numbers[i] + numbers[j])
            
    answer = sorted(list(zero))
    
    return answer
