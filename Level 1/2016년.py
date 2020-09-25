def solution(a, b):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_day = 0
    for month, day in enumerate(month_day):
        if month < a:
            sum_day += day
        elif month == a:
            sum_day += b
    answer = week[(sum_day % 7)]

    return answer

print(solution(5, 24))