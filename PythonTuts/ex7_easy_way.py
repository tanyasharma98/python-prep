#Healthy Programmer
from pygame import mixer
from time import  time
from datetime import datetime
def musicloop(file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        hi = input("")
        if hi==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("water.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    # musicloop("water.mp3","stop")
    ini_water = time()
    ini_eyes = time()
    ini_excer = time()
    water = 5 # 40*60
    eyes = 10 #30*60
    excer = 15 # 45*60

    while True:
        if time()-ini_water > water:
            print(f"drop: to stop")
            musicloop("water.mp3","drop")
            ini_water = time()
            log_now("Drank water at ")

        if time()-ini_eyes > eyes:
            print(f"dodo: TO stop")
            musicloop("eyes.mp3","dodo")
            ini_eyes = time()
            log_now("Eye Excercise at ")

        if time()-ini_excer > excer:
            print("ding:To stop")
            musicloop("physical.mp3","ding")
            ini_excer = time()
            log_now("Excersice at ")