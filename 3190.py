from collections import defaultdict


N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

# 사과 1, 빈곳 0, 뱀 2
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

L = int(input())
time_dir_data = defaultdict(str)
for _ in range(L):
    t, d = input().split()
    time_dir_data[int(t)] = d

# ULDR
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def move_head(rotate, x, y, dir_idx):
    # 오른쪽 회전
    if rotate == 'D':
        if dir_idx == 0:
            next_dir_idx = 3
        else:
            next_dir_idx = dir_idx - 1
    # 왼쪽 회전
    else:
        if dir_idx == 3:
            next_dir_idx = 3
        else:
            next_dir_idx = dir_idx + 1
    return x+dx[next_dir_idx], y+dy[next_dir_idx], next_dir_idx


def run():
    x, y = 0, 0
    time = 0
    cur_dir_idx = 3
    snake = [(0, 0)]
    while True:
        # 다음 칸의 위치
        if time_dir_data[time]:
            cur_rotate = time_dir_data[time]
            nx, ny, cur_dir_idx = move_head(cur_rotate, x, y, cur_dir_idx)
        else:
            nx, ny = x + dx[cur_dir_idx], y + dy[cur_dir_idx]
        time += 1
        # 끝나는 조건
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            return time
        else:
            # 다음 칸 확인
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake = [(nx, ny)] + snake
            else:
                board[nx][ny] = 2
                snake = [(nx, ny)] + snake
                tx, ty = snake.pop()
                board[tx][ty] = 0
        x, y = nx, ny


board[0][0] = 2
ans = run()
print(ans)