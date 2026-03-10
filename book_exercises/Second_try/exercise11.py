
def getHoursMinutesSeconds(totalSeconds):
    secondsRemaining = totalSeconds
    hms = []
    if secondsRemaining == 0:
        return '0s'
    if secondsRemaining >= 3600:
        hours = int(secondsRemaining / 3600)
        secondsRemaining -= hours*3600
        hms.append(str(hours) + 'h')
    if secondsRemaining >= 60:
        minutes = int(secondsRemaining / 60)
        secondsRemaining -= minutes*60
        hms.append(str(minutes) + 'm')
    if secondsRemaining < 60 and secondsRemaining > 0:
        hms.append(str(secondsRemaining) + 's')

    return ' '.join(hms)


names = ['Ana', 'Thiago', 'Mário', 'Moraes']
print(', '.join(names), end='.')
# assert getHoursMinutesSeconds(30) == '30s'
# assert getHoursMinutesSeconds(60) == '1m'
# assert getHoursMinutesSeconds(90) == '1m 30s'
# assert getHoursMinutesSeconds(3600) == '1h'
# assert getHoursMinutesSeconds(3601) == '1h 1s'
# assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
# assert getHoursMinutesSeconds(90042) == '25h 42s'
# assert getHoursMinutesSeconds(0) == '0s'
