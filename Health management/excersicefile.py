from datetime import timedelta
from datetime import datetime
from pygame import mixer

def excercise():
    
    mixer.init()
    
    
    mixer.music.load('excersice.mp3')
    print("playing music")
    mixer.music.set_volume(0.5)
    
    
    mixer.music.play()
    
    print("do 'excdone' to stop")
    userInput = input(" ") 
    while True:
        if userInput != "excdone":
            print("do 'excdone' to stop")
        elif userInput == "excdone":
            mixer.music.stop()
            run_it_now = now + timedelta(minutes=73)
            delay_exc = (run_it_now-now).total_seconds()
            import threading
            threading.Timer(delay_exc, excercise).start()
run_it_now = now + timedelta(minutes=73)
delay_exc = (run_it_now-now).total_seconds()
import threading
threading.Timer(delay_exc, excercise).start()