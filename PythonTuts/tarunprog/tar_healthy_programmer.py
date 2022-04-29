from pygame import mixer
from datetime import datetime
import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break


def log(msg):
    with open("user_info.txt", "a") as f:
        f.write(f"{msg}  at  {datetime.now()}")
        print("Good")
