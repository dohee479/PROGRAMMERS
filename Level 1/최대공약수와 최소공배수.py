def gcd(small, big):
    if small > big:
        small, big = big, small
    while small:
        big, small = small, big % small
    return big


def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    lcm = n * m // gcd(n, m)
    answer.append(lcm)
    return answer


print(solution(3, 12))