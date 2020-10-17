def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else:
            if i == 0:
                i = 11
            l_dis = abs(i - left)
            r_dis = abs(i - right)
            if sum(divmod(l_dis, 3)) > sum(divmod(r_dis, 3)):
                answer += 'R'
                right = i
            elif sum(divmod(l_dis, 3)) < sum(divmod(r_dis, 3)):
                answer += 'L'
                left = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))