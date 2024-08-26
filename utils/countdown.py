import sys
import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r' + time_format)
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print('\r倒计时结束!')
