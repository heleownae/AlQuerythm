def solution(arr1, arr2):
    result = []  
    # 행의 수만큼 반복
    for i in range(len(arr1)):
        row = []        
        # 열의 수만큼 반복
        for j in range(len(arr1[0])):
            sum_result = arr1[i][j] + arr2[i][j]
            row.append(sum_result)        
        result.append(row)    
    return result

def solution(arr1, arr2):             
    return [[arr1[a][b] + arr2[a][b] for b in range(len(arr1[a]))] for a in range(len(arr1))]
