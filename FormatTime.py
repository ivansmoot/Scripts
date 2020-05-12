def formatTime (time):
    time = time.replace('.', ':')
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    second = time.split(':')[2]
    res = int(hour)*60*60 + int(minute)*60 + int(second)
    return res

def formatformatTime(time):
    hour = time // 3600
    minute = time // 60
    second = time - hour*3600 - minute*60
    return '{}:{}:{}'.format(hour, minute, second)

def finalformatTime(time1, time2):
    ftime = formatTime(time1)
    ltime = formatTime(time2)
    res = formatformatTime(ltime - ftime)
    return res


