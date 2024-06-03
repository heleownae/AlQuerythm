from math import ceil
# ceil(x) :  x이상의 수 중, 가장 작은 정수를 반환. 즉, x를 올림하여 반환하는 함수

def solution(progresses, speeds):
    # 배포 수
    answer = []
    # 각 작업의 완료까지 걸린 일수
    complete = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    
    # 현재 배포 그룹의 첫 번째 작업의 완료일
    current = complete[0]
    # 현재 배포 그룹에 포함된 작업의 수
    count = 0
    
    for day in complete:
        # 현재 작업day가 현재 배포 그룹의 첫 번째 작업current보다 더 늦게 완료된다면,
        # 현재까지의 배포 그룹을 answer에 추가하고 새로운 배포 그룹을 시작
        if day > current:
            answer.append(count)
            current = day
            count = 1
        else:
            # 현재 작업이 현재 배포 그룹에 포함되면, 작업 수를 증가
            count += 1
    
    # 마지막 배포 그룹을 answer에 추가
    answer.append(count)
    
    return answer
