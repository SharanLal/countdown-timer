import time

def set_countdown(countdown):
    while countdown:
        mins, secs = divmod(countdown, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end ="\r")
        time.sleep(1)
        countdown -= 1
    
countdown = input("Enter time in seconds: ")

set_countdown(int(countdown)) 