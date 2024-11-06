def add_time(start, duration, day = None):
    output = []

    if start.split(' ')[1] == 'PM':
        first_time = str(int([start.split(':')[0] + start.split(':')[1]][0].split(' ')[0]) + 1200)
    
    else:
        first_time = [start.split(':')[0] + start.split(':')[1]][0].split(' ')[0]

    total_time = int(first_time) + int(duration.split(' ')[0].split(':')[0] + duration.split(' ')[0].split(':')[1])

    loop = 0
    ampm = 0

    while total_time >= 1200:
        total_time -= 1200
        loop += 0.5
        ampm += 1

    if int(str(total_time)[1:]) > 60 and total_time < 1200:
        total_time = total_time - 60 + 100
        
    if total_time > 1200:
        loop += 0.5
        ampm += 1

    total_time = [str(total_time)[:-2] + ':' + str(total_time)[-2:], 'AM' if ampm % 2 == 0 else 'PM']
    output.append(total_time)

    day_num = loop % 7

    if day is not None:
        day = day.lower()
        if day == 'sunday':
            day = 1 + day_num
        elif day == 'monday':
            day = 2 + day_num
        elif day == 'tuesday':
            day = 3 + day_num
        elif day == 'wednesday':
            day = 4 + day_num
        elif day == 'thursday':
            day = 5 + day_num
        elif day == 'friday':
            day = 6 + day_num
        elif day == 'saturday':
            day = 7 + day_num
        day = day % 7
        if day < 2:
            day = 'Sunday'
        elif day < 3:
            day = 'Monday'
        elif day < 4:
            day = 'Tuesday'
        elif day < 5:
            day = 'Wednesday'
        elif day < 6:
            day = 'Thursday'
        elif day < 7:
            day = 'Friday'
        elif day < 8:
            day = 'Saturday'
        output.append(day)

    if loop >= 1:
        loop = ['(next day)' if loop == 1 else f'({int(loop)} days later)']
        output.append(loop)

    if len(output) == 3:
        return output[0][0] + ' ' + output[0][1] + ', ' + output[1] + ' ' +  output[2][0]
    elif len(output) == 2 and output[1][0].isalpha():
        return output[0][0] + ' ' + output[0][1] + ', ' + output[1]
    elif len(output) == 2:
        return output[0][0] + ' ' + output[0][1] + ' ' + output[1][0]
    elif len(output) == 1:
        return output[0][0] + ' ' + output[0][1]

solution = add_time('2:59 AM', '24:00')
print(solution)
