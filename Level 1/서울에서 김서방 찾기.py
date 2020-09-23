def solution(seoul):
    answer = ''
    cnt = 0
    for name in seoul:
        if name == 'Kim':
            answer = '김서방은 {}에 있다'.format(cnt)
        cnt += 1
    return answer