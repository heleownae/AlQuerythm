def solution(n, m, section):
        num = 0
        current_position = 0

        for s in section:
            
            # 현재 롤러 위치 계속 업데이트하는 방법
            if current_position < s:
                num += 1  # 롤러 작업당 업데이트
                current_position = s + m - 1  # 롤러의 위치 업데이트

        return num
