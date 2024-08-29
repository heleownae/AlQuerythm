def solution(a, b):
    jj = 31  # 짝수월
    hh = 30  # 홀수월
    uu = 29  # 윤년

    # 일수를 다 더해서 나머지로 요일 계산한다.
    weekday = {1: 'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU'}
    # 각 월의 일수를 리스트로 만든다.
    month = [0, jj, uu, jj, hh, jj, hh, jj, jj, hh, jj, hh, jj]
    # 전월까지의 총 일수 계산한다.
    total = sum(days_in_month[1:a]) + (b)
    # 총 일수를 7로 나눈 나머지를 통해 요일 찾는다.
    result = (total) % 7

    return weekday[result]
