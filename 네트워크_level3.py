def solution(n, computers):
    networks = 0
    visit = [0]*n
    for start in range(n):
        if visit[start] == 1:
            continue
        stack = [start]
        visit[start] = 1
        while stack:
            cur = stack.pop()
            for i in range(n):
                if i == cur:
                    continue
                if computers[cur][i] and not visit[i]:
                    stack.append(i)
                    visit[i] = 1
        networks += 1
    return networks
