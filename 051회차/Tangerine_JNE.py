from collections import Counter

def solution(k, tangerine):
    size = Counter(tangerine)
    
    sorted_size = sorted(size.values(), reverse=True)
    
    # 선택한 서로 다른 귤의 종류 수를 세는 변수
    different_size = 0
    # 선택한 귤의 총 개수를 세는 변수
    total_selected = 0
    
    #  가장 많이 등장하는 귤의 크기부터 선택
    for count in sorted_size:
        total_selected += count
        different_size += 1
        if total_selected >= k:
            break
            
    return different_size
