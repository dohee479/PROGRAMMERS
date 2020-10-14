def solution(numbers, hand):
    answer = ''
    left = 0
    right = 0
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i - 2
        else:
            if abs(i - left) == abs(i - right):
                if hand == "left":
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    left = i
            elif


    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))