from sys import stdin


def solution(n, data):
    start = 0
    end = n - 1
    minv = abs(data[start] + data[end])
    ms, me = start, end
    while start < end:
        total = data[start] + data[end]
        if abs(total) < minv:
            minv = abs(total)
            ms, me = start, end
            if total == 0:
                return ms, me

        # 두 용액의 합이 0에 가까워지도록함
        if total > 0:
            end -= 1
        else:
            start += 1
    return ms, me


if __name__ == '__main__':
    N = int(stdin.readline())
    value_data = list(map(int, stdin.readline().strip().split()))
    value_data = sorted(value_data)
    i, j = solution(N, value_data)
    print(value_data[i], value_data[j])
