def solution(s):
    answer = ''
    # 공백 뒤에 시작하는 문자만 대문자이면 된다.
    for i, word in enumerate(s):
        # 따라서, 맨 앞의 문자와 현재 위치 전의 문자가 공백이면 대문자로 변환했다.
        if i == 0 or s[i - 1] == ' ':
            answer += word.upper()
        # 그 외에는, 소문자로 변환했다.
        else:
            answer += word.lower()
    return answer


print(solution('3people unFollowed me'))
print(solution('for the last week'))