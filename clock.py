import time
import os

def focus_timer(duration):
    """A function that starts a countdown timer for a given duration"""

    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1

    print("Time's up!")
    # Play an alarm sound when the timer ends
    os.system('afplay /System/Library/Sounds/Glass.aiff')

if __name__ == '__main__':
    # Set the duration of the focus timer in seconds (default 25 minutes)
    duration = 60 * 60
    focus_timer(duration)
