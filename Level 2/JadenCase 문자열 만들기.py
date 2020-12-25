def solution(s):
    answer = ''
    for word in s.split():
        word = word[0].upper() + word[1:].lower()
        answer += word + ' '
    return answer.rstrip(' ')


print(solution('3people unFollowed me'))
print(solution('for the last week'))