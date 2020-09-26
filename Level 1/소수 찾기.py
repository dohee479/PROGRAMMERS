# 에라토스테네스의 체 이용
def solution(n):
    multiple = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        # i는 소수인지 판별
        if multiple[i]:
            # i의 배수들 체크
            for j in range(i + i, n + 1, i):
                multiple[j] = False
    answer = multiple.count(True)
    return answer - 2

print(solution(10))