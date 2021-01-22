from itertools import combinations, permutations

def check(u_id_permutation, banned_id):
    for i in range(len(banned_id)):
        if len(u_id_permutatio[i])!=len(banned_id[i]):
            return False
        for j in range(len(u_id_permutatio[i])):
            if banned_id[i][j] == '*':
                continue
            elif u_id_permutatio[i][j] == banned_id[i][j]:
                continue
            else:
                return False
    return True
    

def solution(user_id, banned_id):
    answer = 0
    user_id_combination_list = combinations(user_id, len(banned_id))  # 가능한 user_id 조합
    
    for user_id_combination in user_id_combination_list:
        user_id_permutation_list = permutations(user_id_combination)  # 조합의 원소들로 만들 수 있는 순열
        for user_id_permutation in user_id_permutation_list:
            if check(user_id_permutation, banned_id):
                answer += 1
                break
    return answer