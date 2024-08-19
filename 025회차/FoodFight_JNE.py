def solution(food):
    left = []
    right = []
    
    # 각 음식의 양에 따라 좌측과 우측 배열 생성
    for i in range(1, len(food)):
        # 각 음식의 양을 나누어 좌측과 우측에 음식 추가
        count = food[i] // 2
        left.append(str(i) * count)
        right.append(str(i) * count)
    
    # 좌측과 우측을 결합하고 물 추가
    # right는 반대로 추가하므로 reverse() 사용
    return ''.join(left) + '0' + ''.join(right[::-1])
