def solution(s):
    answer = ''
    for i, word in enumerate(s):
        if i == 0 or s[i - 1] == ' ':
            answer += word.upper()
        else:
            answer += word.lower()
    return answer


print(solution('3people unFollowed me'))
print(solution('for the last week'))