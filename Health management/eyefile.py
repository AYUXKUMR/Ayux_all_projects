from datetime import timedelta
from datetime import datetime
from pygame import mixer

def eye():
    
    mixer.init()
    
    mixer.music.load("eye.mp3")
    print("playing music")
    mixer.music.set_volume(0.5)
    
    mixer.music.play()
    
    print("do 'eyedone' to stop")
    userInput = input(" ")
    while True:
        if userInput != 'eyedone':
            print("do 'eyedone' to stop")
        elif userInput == 'eyedone':
            mixer.music.stop()
            run_it = now + timedelta(minutes=53)
            delay_eye = (run_it-now).total_seconds()
            import threading
            threading.Timer(delay_eye, eye).start()
            
            
run_it = now + timedelta(minutes=53)
delay_eye = (run_it-now).total_seconds()
import threading
threading.Timer(delay_eye, eye).start()