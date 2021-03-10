def solution(n):
    cnt_one = bin(n)[2:].count('1')
    for i in range(n + 1, 2 * n):
        if cnt_one == bin(i)[2:].count('1'):
            return i


print(solution(78))