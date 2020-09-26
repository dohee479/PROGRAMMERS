# 에라토스테네스의 체 이용
# 이게 더 빠름
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

def solution(n):
    num = set(range(2, n+1))

    root = n ** 0.5
    for i in range(2, root + 1):
        if i in num:
            num -= set(range(2 * i, n+1, i))
    return len(num)

print(solution(10))