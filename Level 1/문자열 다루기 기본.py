def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in '1234567890':
                return False
        return True
    return False

print(solution("234 48"))

def solution(s):
    return s.isdigit() and len(s) in (4, 6)