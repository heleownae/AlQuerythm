def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    start_x = start_y = -1
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    
    direction = {
        'N': (-1, 0),  # 북쪽
        'S': (1, 0),   # 남쪽
        'W': (0, -1),  # 서쪽
        'E': (0, 1)    # 동쪽
    }
    
    current_x, current_y = start_x, start_y
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        dx, dy = direction[op]
        
        new_x, new_y = current_x, current_y
        
        can_move = True
        for step in range(n):
            new_x += dx
            new_y += dy
            
            if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W:
                can_move = False
                break
            
            if park[new_x][new_y] == 'X':
                can_move = False
                break
        
        if can_move:
            current_x, current_y = new_x, new_y
    
    return [current_x, current_y]
