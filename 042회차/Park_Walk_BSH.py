start = []
fence = []
limit_a = len(park[0])
limit_b = len(park)

# 초기 위치 및 장애물 위치 설정
for row, parks in enumerate(park):
    for col, word in enumerate(parks):
        if word == 'S':
            start = [row, col]
        elif word == 'X':
            fence.append([row, col])

# 이동 함수 정의
def move(start, direction, steps):
    delta = {
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
        'N': (-1, 0)
    }
    d_row, d_col = delta[direction]
    tmp = start.copy()
    
    for _ in range(steps):
        start[0] += d_row
        start[1] += d_col
        if (start in fence) or (start[0] >= limit_b) or (start[1] >= limit_a) or (start[0] < 0) or (start[1] < 0):
            return tmp  # 장애물 또는 경계에 부딪히면 초기 위치로 복귀
    return start

# 경로 처리
for route in routes:
    direction, num = route.split()
    start = move(start, direction, int(num))

print(start)
