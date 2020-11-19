def solution(priorities, location):
    answer = 0
    queue = []
    for i, value in enumerate(priorities):
        queue.append((i, value))
    while queue:
        important = max(queue, key=lambda x: x[1])
        printing = queue.pop(0)
        if printing[1] < important[1]:
            queue.append((printing[0], printing[1]))
        else:
            answer += 1
            if printing[0] == location:
                return answer