def solution(s):
    answer = sorted(s, reverse=True)
    return ''.join(map(str, answer))

print(solution('Zbcdefg'))