def solution(triangle):
    N = len(triangle)
    dp = [[0] * (N + 2) for _ in range(N)]  # 현재 위치까지의 최대합
    dp[0][1] = triangle[0][0]
    for i in range(1, N):
        for j in range(1, i + 2):
            # 올 수 있는 경로의 최대합 + 현재 위치 값
            dp[i][j] = max(dp[i - 1][j-1] + triangle[i][j-1], dp[i - 1][j] + triangle[i][j-1])
    answer = max(dp[N-1])
    return answer
