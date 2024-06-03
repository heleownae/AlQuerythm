from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 1             # 작업 일자
    distribution = 0    # 현재 배포 주기에서 완료된 작업 수
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # progresses 큐가 빌 때까지 반복
    while progresses:
        # 작업률이 100 이상이면 큐에서 제거 및 완료된 작업 수 증가
        if progresses[0] + day * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            distribution += 1
        else:
            # 현재 작업이 끝나지 않았는데, distribution에 완료된 작업이 있다면 answer에 완료된 작업의 개수를 추가하고 배포 진행
            if distribution > 0:
                answer.append(distribution)
                distribution = 0
            day += 1    # 작업 일자 증가

    # 마지막 작업까지 완료했을 때, 아직 distribution이 남아있다면 answer에 마지막으로 배포할 작업의 개수 추가
    if distribution > 0:
        answer.append(distribution)
    
    return answer
