def solution(lottos, win_nums):
    # 알아볼 수 없는 번호의 개수 세기
    zero = lottos.count(0)
    # 당첨 번호와 일치하는 번호 수 - 교집합
    match = len(set(lottos) & set(win_nums))
    
    # 최고 순위와 최저 순위 계산
    max_rank = 7 - (match + zero)  # 최고 순위
    min_rank = 7 - match  # 최저 순위
    
    # 7등 없애기
    max_rank = min(max_rank, 6)
    min_rank = min(min_rank, 6)
    
    return [max(1, max_rank), max(1, min_rank)]
