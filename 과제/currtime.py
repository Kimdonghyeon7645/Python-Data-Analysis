import time


def getTime() -> tuple:
    tm = time.localtime(time.time())
    return tm.tm_hour, tm.tm_min, tm.tm_sec
