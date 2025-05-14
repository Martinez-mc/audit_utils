from datetime import datetime, timedelta

def time_dif(enter, exit):

    time_format = '%H:%M:%S'
    time_delta = datetime.strptime(exit, time_format) - datetime.strptime(enter, time_format) - timedelta(hours=1)
    return time_delta

t1 = '8:30:00'
t2 = '12:00:00'

print(time_dif(t1, t2))