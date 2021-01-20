def solution(numbers, target):

    def dfs(index, total, cnt):
        if index == len(numbers):
            if total == target:
                cnt += 1
                return cnt
            else:
                return 0
        else:
            ans1 = dfs(index+1, total+numbers[index], cnt)
            ans2 = dfs(index+1, total-numbers[index], cnt)
            return ans1+ans2

    answer = dfs(0, 0, 0)
    return answer
