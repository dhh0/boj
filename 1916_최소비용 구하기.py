from sys import stdin
from collections import defaultdict
import math
import heapq
input = lambda :stdin.readline().strip()  # 이거 안해서 계속 시간 초과
N = int(input())
M = int(input())
graph = defaultdict(list)
visited = [0]*(N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
start, end = map(int, input().split())
INF = math.inf
dp = [INF]*(N+1)


def dijkstra(start):
    dp[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))  # (우선 순위, 값) 순서 바꿔서 넣으면 안됨, 그냥 튜플 아님
    # 가까운 순서대로 처리
    while pq:
        cost, current = heapq.heappop(pq)
        # 지금 꺼낸 것보다 더 짧은 경로를 알고 있다면 지금 꺼낸 것을 무시
        if dp[current] < cost:
            continue
        # 인접한 정점들을 모두 검사
        for node, w in graph[current]:
            next_cost = cost + w
            # 더 짧은 경로를 발견하면, dp를 갱신하고 우선순위 큐에 넣는다.
            if next_cost < dp[node]:
                dp[node] = next_cost
                heapq.heappush(pq, (next_cost, node))


dijkstra(start)
print(dp[end])



