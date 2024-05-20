def can_fit(N, L, W, H, A):
    num_L = L // A
    num_W = W // A
    num_H = H // A
    total_boxes = num_L * num_W * num_H
    
    return total_boxes >= N

def find_max_A(N, L, W, H):
    left = 0.0
    right = min(L, W, H)
    precision = 1e-9
    max_iterations = 1000

    for _ in range(max_iterations):
        mid = (left + right) / 2.0
        if can_fit(N, L, W, H, mid):
            left = mid
        else:
            right = mid
        
        if right - left < precision:
            break
    
    return left

N, L, W, H = map(int, input().split())

max_A = find_max_A(N, L, W, H)
print(f"{max_A:.10f}")