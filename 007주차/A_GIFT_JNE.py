# 큰 박스에 넣을 수 있는 선물 갯수 확인
def big_box(N, L, W, H, A):
    return (L // A) * (W // A) * (H // A) >= N

def find_A(N, L, W, H):
    low, high = 1, max(L, W, H)
    # 충분히 작은 오차 범위 내에서 반복을 종료하기 위함
    while high - low > 0:
        mid = (low + high) / 2
        if big_box(N, L, W, H, mid):
            low = mid
        else:
            high = mid
    return low

N, L, W, H = map(int, input().split())

max_A = find_A(N, L, W, H)

print(round(max_A, 1))
# 시간 초과, 무한루프



# 큰 박스에 넣을 수 있는 선물 갯수 확인
def big_box(N, L, W, H, A):
    return (L // A) * (W // A) * (H // A) >= N

def find_A(N, L, W, H):
    low, high = 1, max(L, W, H)
    
    while high - low > 1e-9:
        mid = (low + high) / 2
        if big_box(N, L, W, H, mid):
            low = mid
        else:
            high = mid
    return low

N, L, W, H = map(int, input().split())

max_A = find_A(N, L, W, H)

print(round(max_A, 15))
# 시간 초과?
