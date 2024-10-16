def solution(wallpaper):
    min_row = float('inf')
    max_row = float('-inf')
    min_col = float('inf')
    max_col = float('-inf')
    
    # wallpaper를 순회하면서 파일의 위치를 찾음
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
     
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
                    
    return [min_row, min_col, max_row + 1, max_col + 1]
