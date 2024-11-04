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
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    current_x, current_y = start_x, start_y
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        dx, dy = direction[op]
        
        valid_move = True
        for step in range(1, n + 1):
            new_x = current_x + dx * step
            new_y = current_y + dy * step
            
            if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W or park[new_x][new_y] == 'X':
                valid_move = False
                break
        
        if valid_move:
            current_x += dx * n
            current_y += dy * n
    
    return [current_x, current_y]
