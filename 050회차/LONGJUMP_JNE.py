def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # dp는 각 칸에 도달하는 방법의 수 저장
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    return dp[n]
