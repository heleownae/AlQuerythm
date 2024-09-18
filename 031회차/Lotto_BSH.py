def solution(lottos, win_nums):
    ranking = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    # 맞춘 숫자 개수 세기
    correct = sum(1 for i in lottos if i in win_nums)
    
    # 최고 순위는 0을 모두 맞췄을 경우, 최저 순위는 현재 맞춘 숫자만으로 계산한다.
    max_rank = ranking[correct + lottos.count(0)]
    min_rank = ranking[correct]

    return [max_rank, min_rank]
