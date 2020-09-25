def solution(s):
    low_s = s.lower()
    if low_s.count('p') or low_s.count('y'):
        if low_s.count('p') == low_s.count('y'):
            answer = True
        else:
            answer = False
    else:
        answer = True

    return answer

print(solution('pPoooyY'))

def solution(s):
    return s.lower().count('p') == s.lower().count('y')