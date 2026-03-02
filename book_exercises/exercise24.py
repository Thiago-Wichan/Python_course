# E X E R C I S E # 2 4 : E V E R Y 1 5 M I N U T E S
hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
minutes = [00, 15, 30, 45]
day_time = ['am', 'pm']


def american_clock():
    for times in day_time:
        for hour in hours:
            for minute in minutes:
                print(f'{hour:02d}:{minute:02d} {times}')


american_clock()
