def solution(n, lost, reserve):
    rest=sorted(reserve.copy())  # 1. 최댓값을 출력하기 위해 오름차순 정렬하기
    for i in reserve:
        if i in lost:
            lost.remove(i)
            rest.remove(i)  # 2. 여벌을 가져왔으나 도난 당한 학생 필터링하기
    for i in rest:
        cnt=0  # 3. 여벌번호에 해당하면 도난 당한 학생 리스트에서 제거하기
        if i-1 in lost:
            lost.remove(i-1)
            cnt+=1
        if cnt==0 and i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)  # 4. 최종 학생수 출력하기
