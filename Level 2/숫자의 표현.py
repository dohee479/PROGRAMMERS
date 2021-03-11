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


# n이 주어졌을 때, 1부터 n까지의 수 중 홀수이면서 n의 약수인 개수를 구한다.
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])