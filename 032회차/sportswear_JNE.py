def solution(n, lost, reserve):
    students = [1] * (n + 1) 
    
    #  도난당한 체육복 수
    for student in lost:
        students[student] -= 1
    
    # 여벌 체육복 수
    for student in reserve:
        students[student] += 1
    
    # 대여
    for student in range(1, n + 1):
    # 체육복 없다면,
        if students[student] == 0:
        # 앞번호 대여
            if student > 1 and students[student - 1] == 2:
                students[student] += 1
                students[student - 1] -= 1
                # 뒷번호 대여
            elif student < n and students[student + 1] == 2:
                students[student] += 1
                students[student + 1] -= 1
    
    # 체육복 수 계산
    answer = sum(1 for student in range(1, n + 1) if students[student] > 0)
    
    return answer
