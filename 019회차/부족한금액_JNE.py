def solution(price, money, count):
    # count 만큼 탈 때 전체 비용
    cost = price * count * (count + 1) // 2
    # 넉넉할 때 0, 부족할 때 비용 - 가진 돈 하면 양수로 출력 될 것
    return max(0, cost - money)
