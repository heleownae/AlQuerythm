def solution(number):
    count = 0
    length = len(number)    
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    return count
