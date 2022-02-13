import time

def timestamp_now() -> int:
    return int(time.mktime(time.localtime()))

def timestamp(
    string: str,
    form: str = '%Y-%m-%d %H:%M:%S'
) -> int:
    return int(time.mktime(time.strptime(string, form)))

def natural_date(
    timestamp: int, 
    form: str = '%Y-%m-%d %H:%M:%S'
) -> str:
    if timestamp < 0:
        return None
    res = time.localtime(int(timestamp))
    return time.strftime(form, res)

def natural_time(timestamp: int) -> str:
    s = timestamp % 60
    m = (timestamp % 3600) // 60
    h = timestamp // 3600
    return f'{h} h {m} m {s} s'