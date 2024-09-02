def solution(cards1, cards2, goal):
    i, j = 0, 0
    
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"
    return "Yes"

"""
1. goal을 돌면서, 현재 단어가 card1의 현재 인덱스와 일치하면, i를 1씩 증가
2. goal을 돌면서, 현재 단어가 card2의 현재 인덱스와 일치하면, j를 1씩 증가
3. 일치하는 단어가 없으면, No 출력
4. 모든 단어가 처리될 수 있으면, Yes 출력
"""
