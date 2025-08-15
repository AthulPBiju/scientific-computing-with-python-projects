def add_time(start, duration, day=None):

    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    start_hours=int(start.split(':')[0])
    start_min=int(start.split(':')[1][:2])
    start_meridian=start.split(':')[1][-2:]

    duration_hours=int(duration.split(':')[0])
    duration_min=int(duration.split(':')[1])

    if start_meridian=='PM':
        start_hours+=12
    elif start_meridian=='AM' and start_hours==12:
        start_hours=0

    total_hours=start_hours+duration_hours
    total_min=start_min+duration_min

    total_hours+=total_min//60
    total_min%=60
    
    extra=total_hours//24
    total_hours%=24

    #Meridian
    MERIDIAN='PM' if total_hours>=12 else 'AM'
    #Hours
    if total_hours==0:
        HOURS='12'
    elif total_hours>12:
        HOURS=str(total_hours-12)
    else:
        HOURS=str(total_hours)
    #Minutes
    MINUTES=str(total_min)
    if len(MINUTES)==1:
        MINUTES='0'+MINUTES
    #Day
    if day!=None:
        n=days.index(day.title())
        no=n+extra
        no%=7
        DAY=', '+days[no]
    else:
        DAY=''
    #Text
    if extra==0:
        TEXT=''
    elif extra==1:
        TEXT=' (next day)'
    else:
        TEXT=f' ({extra} days later)'

    new_time=f'{HOURS}:{MINUTES} {MERIDIAN}{DAY}{TEXT}'

    return new_time
print(add_time('2:59 AM', '24:00', 'saturDay'))