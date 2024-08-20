def solution(a, b, n):
# 총 받은 콜라의 병 수
    total_cola = 0  
    # 처음 가지고 있는 빈 병 수
    empty = n  

    while empty >= a:
        # 현재 빈 병으로 받을 수 있는 콜라 병 수
        new_cola = (empty // a) * b
        total_cola += new_cola
        
        # 사용한 빈 병 수와 새로 생긴 빈 병 수를 계산
        # 남은 빈 병 + 새로 받은 빈 병
        empty = empty % a + new_cola  

    return total_cola
