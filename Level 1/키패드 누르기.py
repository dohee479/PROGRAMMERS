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
            l_dis = abs(i - left)
            r_dis = abs(i - right)
            if l_dis == 3:
                l_dis = 1
            if l_dis == 6:
                l_dis = 2
            if r_dis == 3:
                r_dis = 1
            if r_dis == 3:
                r_dis = 2
            if l_dis == r_dis:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
            elif l_dis > r_dis:
                answer += 'R'
                right = i
            else:
                answer += 'L'
                left = i
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))