def solution(n):
    answer = 0
    for i in range(1, 10001):
        sum_num = i
        if i > n:
            break
        if sum_num == n:
            answer += 1
            break
        for j in range(i + 1, 10001):
            sum_num += j
            if sum_num > n:
                break
            if sum_num == n:
                answer += 1
                break
    return answer


print(solution(15))