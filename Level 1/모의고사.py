def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    f_score = 0
    s_score = 0
    t_score = 0
    for i in range(len(answers)):
        if i % 5 == 0:
            if answers[i] == first[0]:
                f_score += 1
        elif i % 5 == 1:
            if answers[i] == first[1]:
                f_score += 1
        elif i % 5 == 2:
            if answers[i] == first[2]:
                f_score += 1
        elif i % 5 == 3:
            if answers[i] == first[3]:
                f_score += 1
        elif i % 5 == 4:
            if answers[i] == first[4]:
                f_score += 1

    for i in range(len(answers)):
        if i % 8 == 0:
            if answers[i] == second[0]:
                s_score += 1
        elif i % 8 == 1:
            if answers[i] == second[1]:
                s_score += 1
        elif i % 8 == 2:
            if answers[i] == second[2]:
                s_score += 1
        elif i % 8 == 3:
            if answers[i] == second[3]:
                s_score += 1
        elif i % 8 == 4:
            if answers[i] == second[4]:
                s_score += 1
        elif i % 8 == 5:
            if answers[i] == second[5]:
                s_score += 1
        elif i % 8 == 6:
            if answers[i] == second[6]:
                s_score += 1
        elif i % 8 == 7:
            if answers[i] == second[7]:
                s_score += 1

    for i in range(len(answers)):
        if i % 10 == 0:
            if answers[i] == third[0]:
                t_score += 1
        elif i % 10 == 1:
            if answers[i] == third[1]:
                t_score += 1
        elif i % 10 == 2:
            if answers[i] == third[2]:
                t_score += 1
        elif i % 10 == 3:
            if answers[i] == third[3]:
                t_score += 1
        elif i % 10 == 4:
            if answers[i] == third[4]:
                t_score += 1
        elif i % 10 == 5:
            if answers[i] == third[5]:
                t_score += 1
        elif i % 10 == 6:
            if answers[i] == third[6]:
                t_score += 1
        elif i % 10 == 7:
            if answers[i] == third[7]:
                t_score += 1
        elif i % 10 == 8:
            if answers[i] == third[8]:
                t_score += 1
        elif i % 10 == 9:
            if answers[i] == third[9]:
                t_score += 1
    max_score = max(f_score, s_score, t_score)
    if max_score == f_score:
        answer.append(1)
    if max_score == s_score:
        answer.append(2)
    if max_score == t_score:
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))

