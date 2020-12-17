def solution(people, limit):
    answer = 0
    people.sort()
    for i in range(len(people)):
        if i:
            if i != len(people) - 1:
                if people[i - 1] + people[i] <= limit:
                    continue
                if people[i] + people[i + 1] <= limit:
                    answer += 1
                else:
                    answer += 1
            else:
                if people[i - 1] + people[i] > limit:
                    answer += 1
        else:
            answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))