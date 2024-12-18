def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)
points = 2
