# 지독한 반례찾기
def solution(n, lost, reserve):
    rest=sorted(reserve.copy())  # 최댓값 출력을 위해 우선 정렬하기

    for i in reserve:
        if i in lost:
            lost.remove(i)
            rest.remove(i)  # 여벌을 가져왔으나 도난 당한 학생 필터링하기

    for i in rest:
        cnt=0
        if i-1 in lost:
            lost.remove(i-1)
            cnt+=1
        if cnt==0 and i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)
