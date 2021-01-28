# 오르막 수
import sys
N = int(sys.stdin.readline().strip())


def solution(n):
    dp = [k for k in range(10, 0, -1)]
    if n == 1:
        return 10

    if n == 2:
        return sum(dp)

    for _ in range(3, n+1):
        for idx in range(10):
            dp[idx] = sum(dp[idx:])
    return sum(dp)


print(solution(N) % 10007)
