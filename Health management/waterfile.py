from datetime import timedelta
from datetime import datetime
from pygame import mixer

now = datetime.now()
def water():
    
	mixer.init()

	mixer.music.load('water.mp3')

	print("playing water sound")
	mixer.music.set_volume(0.5)
	mixer.music.play()

	# pause syestem
	print("do 'drank' to stop")
	while True:
		userInput = input(" ")
		if userInput != "drank":
			print("do 'drank' to stop")
		elif userInput == "drank":
			mixer.music.stop()
			run = now + timedelta(minutes=23)
			delay = (run-now).total_seconds()
			import threading
			threading.Timer(delay, water).start()
		

run = now + timedelta(minutes=23)
delay = (run-now).total_seconds()
import threading
threading.Timer(delay, water).start()
		

            




    
