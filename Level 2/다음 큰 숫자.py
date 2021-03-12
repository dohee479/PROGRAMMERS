def solution(n):
    cnt_one = bin(n)[2:].count('1')
    for i in range(n + 1, 2 * n):
        if cnt_one == bin(i)[2:].count('1'):
            return i


print(solution(78))


# 내가 짠 코드와 로직은 같다.
# while문으로 조건을 걸어 범위를 주지 않았다.
def countone(n):
    return bin(n).count('1')


def nextBigNumber(n):
    i = 1
    while countone(n) != countone(n+i):
        i += 1
    return n + i
