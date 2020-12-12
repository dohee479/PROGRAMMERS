def solution(s):
    return '{} {}'.format(min(map(int, s.split())), max(map(int, s.split())))


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
print(solution('-1 -1'))