def solution(strings, n):
    answer = []
    strings.sort()
    for i in range(len(strings)-1, -1, -1):
        for j in range(i):
            if strings[j][n] > strings[j+1][n]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
            # if strings[j][n] == strings[j+1][n]:
            #     if strings[j] > strings[j+1]:
            #         strings[j], strings[j+1] = strings[j+1], strings[j]
    answer = strings
    return answer