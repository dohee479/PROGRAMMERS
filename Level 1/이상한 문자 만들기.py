def solution(s):
    answer = ''
    arr = s.split(' ')
    for i, voca in enumerate(arr):
        for j, letter in enumerate(voca):
            if j % 2:
                answer += letter.lower()
            else:
                answer += letter.upper()
        if i != len(arr) - 1:
            answer += ' '
    return answer


print(solution('try hello world'))