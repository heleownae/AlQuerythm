# 백준 3003번 - 킹, 퀸, 룩, 비숍, 나이트, 폰 (이해원)
# https://www.acmicpc.net/problem/3003

# 입력값 -> 공백으로 나눔 -> int로 바꿈 -> 리스트에 넣음
input_list = list(map(int, input().split()))

# 흰색 피스 개수
white_list = [1, 1, 2, 2, 2, 8]

for i, j in zip(white_list, input_list):
    print(i - j, end=' ')