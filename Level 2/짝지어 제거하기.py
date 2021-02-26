def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            s = s[:i + 1] + s[i + 1:]

    return answer


print(solution('baabaa'))