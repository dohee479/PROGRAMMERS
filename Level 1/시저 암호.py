def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        # isupper(), islower() 대체할수 있다
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ord(i) + n <= 90:
                answer += chr(ord(i) + n)
            else:
                answer += chr(ord(i) + n - 26)
        else:
            if ord(i) + n <= 122:
                answer += chr(ord(i) + n)
            else:
                answer += chr(ord(i) + n - 26)

    return answer

print(solution("a B z", 4))