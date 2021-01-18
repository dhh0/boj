from sys import stdin

n, m = map(int, stdin.readline().strip().split())
row, col = [], []

for _ in range(m):
    i, j = map(int, stdin.readline().strip().split())
    row.append(i)
    col.append(j)

# 최소거리가 되는 위치 => 중앙값
mid_x = sorted(row)[m//2]
mid_y = sorted(col)[m//2]

min_dist = 0
for k in range(m):
    min_dist += abs(mid_x - row[k]) + abs(mid_y - col[k])

print(min_dist)