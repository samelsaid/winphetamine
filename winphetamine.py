import ctypes
from time import sleep
from sys import argv
from itertools import zip_longest

ES_CONTINUOUS = 0x80000000
ES_DISPLAY_REQUIRED = 0x00000002

def countdown_viewer(seconds):
    return f"{seconds // 3600:02}:{(seconds % 3600) // 60 :02}:{seconds % 60:02}"

def duration_maker(hours = 0, minutes = 0, seconds = 0):
    return int((hours * 3600) + (minutes * 60) + seconds)

def keep_awake(time_h, time_m, time_s):
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED)

        duration = duration_maker(hours = time_h, minutes=time_m, seconds=time_s)

        for i in range(duration, 0,  -1):
            sleep (1)
            # replace all + with 000 in unicode !!!
            print("\r", countdown_viewer(i), "\U0001F680" , end="") # unicode for 🚀

        print(countdown_viewer(i))
    except KeyboardInterrupt:
        print("\nSheesh, you don't have to be so rude...find a better way to exit")
    finally:
        print("\U0001F634") # unicode for 😴
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)


def test(time_h, time_m, time_s):
    print(countdown_viewer(duration_maker(hours = time_h, minutes=time_m, seconds=time_s)))

if __name__ == "__main__" :
    duration = argv[1].split(":")
    timer = {
        "hours" : 0,
        "mins" : 0,
        "secs" : 0
    }
    try:
        for time_key, time_value in zip_longest(timer, duration, fillvalue=0):
            timer[time_key] = int(time_value)
        
        keep_awake(*timer.values())
        

        # test(*timer.values())
    except Exception as e:
        print("Provide the time in hours:minutes:seconds -- you can enter hours without minutes, etc\n", f"Error: {e}")
