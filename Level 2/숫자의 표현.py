def solution(n):
    answer = 1
    for i in range(1, (n // 2) + 1):
        sum_num = i
        for j in range(i + 1, (n // 2) + 2):
            sum_num += j
            if sum_num > n:
                break
            if sum_num == n:
                answer += 1
                break
    return answer


print(solution(15))