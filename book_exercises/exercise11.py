# E X E R C I S E # 1 1 : H O U R S , M I N U T E S , S E C O N D S

def getHoursMinutesSeconds(totalseconds):
    remaining_time = totalseconds
    time = []
    while remaining_time > 0:
        hour_calculate = remaining_time // 3600
        if hour_calculate > 0:
            time.append(f'{hour_calculate}h')
            remaining_time -= hour_calculate * 3600
        minutes_calculate = remaining_time // 60
        if minutes_calculate > 0:
            time.append(f'{minutes_calculate}m')
            remaining_time -= minutes_calculate * 60
        if remaining_time > 0:
            time.append(f'{remaining_time}s')
            remaining_time -= remaining_time

        return ' '.join(time)
    return '0s'


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
